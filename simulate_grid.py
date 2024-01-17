#!/usr/bin/env python3
"""
Distribution Grid Day-Ahead Simulation
Simulates 24 hours for a small feeder with base load, rooftop PV, and battery storage.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_profiles():
    """Load CSV profiles for base load, PV generation, and battery specs."""
    base_load = pd.read_csv('profiles/base_load.csv')
    pv_gen = pd.read_csv('profiles/pv_generation.csv')
    battery_specs = pd.read_csv('profiles/battery_specs.csv')
    return base_load, pv_gen, battery_specs

def calculate_net_load(base_load, pv_gen):
    """Calculate net load (load - PV generation) for each hour."""
    net_load = base_load['load_kw'].values - pv_gen['pv_kw'].values
    return net_load

def initialize_battery(battery_specs):
    """Initialize battery state."""
    capacity = battery_specs[battery_specs['parameter'] == 'capacity_kwh']['value'].values[0]
    max_power = battery_specs[battery_specs['parameter'] == 'max_power_kw']['value'].values[0]
    initial_soc = capacity * 0.5  # Start at 50% state of charge
    return {
        'capacity_kwh': capacity,
        'max_power_kw': max_power,
        'soc_kwh': initial_soc
    }

def battery_control(net_load_hour, battery, threshold=6.0, efficiency=0.95):
    """Simple battery control rule to reduce peak load.
    
    Args:
        net_load_hour: Net load for current hour (kW)
        battery: Battery state dict
        threshold: Load threshold above which battery discharges (kW)
    
    Returns:
        battery_power: Positive for discharge, negative for charge (kW)
    """
    battery_power = 0.0
    
    # Discharge battery when net load is high
    if net_load_hour > threshold:
        # Calculate desired discharge power
        desired_discharge = net_load_hour - threshold
        # Limit by battery max power and available energy
        max_discharge = min(battery['max_power_kw'], battery['soc_kwh'])
        battery_power = min(desired_discharge, max_discharge)
    
    # Charge battery when net load is low or negative (excess PV)
    elif net_load_hour < 2.0:
        # Calculate desired charge power
        desired_charge = 2.0 - net_load_hour
        # Limit by battery max power and available capacity
        available_capacity = battery['capacity_kwh'] - battery['soc_kwh']
        max_charge = min(battery['max_power_kw'], available_capacity)
        battery_power = -min(desired_charge, max_charge)  # Negative for charging
    
    return battery_power

def main():
    print("Distribution Grid Simulation Starting...")
    
    # Load profiles
    base_load, pv_gen, battery_specs = load_profiles()
    print(f"Loaded {len(base_load)} hours of data")
    
    # Calculate net load
    net_load = calculate_net_load(base_load, pv_gen)
    print(f"Net load range: {net_load.min():.2f} to {net_load.max():.2f} kW")
    
    # Initialize battery
    battery = initialize_battery(battery_specs)
    print(f"Battery initialized: {battery['capacity_kwh']} kWh capacity, {battery['soc_kwh']} kWh initial SOC")
    
    # Simulation arrays
    hours = base_load['hour'].values
    battery_power = np.zeros(24)  # Battery charge/discharge power (kW)
    battery_soc = np.zeros(24)    # Battery state of charge (kWh)
    grid_power = np.zeros(24)     # Power from/to grid (kW)
    
    # Calculate baseline peak (without battery)
    baseline_peak = np.max(np.abs(net_load))
    print(f"Baseline peak power: {baseline_peak:.2f} kW")
    
    print("\nStarting 24-hour simulation...")
    for hour in hours:
        idx = int(hour)
        # Store current battery SOC
        battery_soc[idx] = battery['soc_kwh']
        
        # Apply battery control
        battery_power[idx] = battery_control(net_load[idx], battery)
        
        # Update battery SOC (1 hour timestep)
        battery['soc_kwh'] -= battery_power[idx]  # Discharge decreases SOC
        battery['soc_kwh'] = np.clip(battery['soc_kwh'], 0, battery['capacity_kwh'])
        
        # Calculate grid power
        grid_power[idx] = net_load[idx] - battery_power[idx]
    
    print("Simulation complete.")
    
    # Calculate final peak with battery
    final_peak = np.max(np.abs(grid_power))
    peak_reduction = baseline_peak - final_peak
    peak_reduction_pct = (peak_reduction / baseline_peak) * 100 if baseline_peak > 0 else 0
    
    # Calculate congestion proxy (sum of squared power flows)
    baseline_congestion = np.sum(net_load ** 2)
    final_congestion = np.sum(grid_power ** 2)
    congestion_reduction = baseline_congestion - final_congestion
    congestion_reduction_pct = (congestion_reduction / baseline_congestion) * 100 if baseline_congestion > 0 else 0
    
    print(f"\nResults:")
    print(f"  Baseline peak: {baseline_peak:.2f} kW")
    print(f"  Final peak: {final_peak:.2f} kW")
    print(f"  Peak reduction: {peak_reduction:.2f} kW ({peak_reduction_pct:.1f}%)")
    print(f"\n  Congestion proxy (sum of squared flows):")
    print(f"    Baseline: {baseline_congestion:.2f}")
    print(f"    Final: {final_congestion:.2f}")
    print(f"    Reduction: {congestion_reduction:.2f} ({congestion_reduction_pct:.1f}%)")

if __name__ == "__main__":
    main()

