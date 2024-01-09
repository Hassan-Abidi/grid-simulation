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
    
    print("\nStarting 24-hour simulation...")
    for hour in hours:
        idx = int(hour)
        # Store current battery SOC
        battery_soc[idx] = battery['soc_kwh']
        
        # Placeholder: no battery control yet
        battery_power[idx] = 0.0
        grid_power[idx] = net_load[idx]
    
    print("Simulation complete.")

if __name__ == "__main__":
    main()

