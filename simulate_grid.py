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

def main():
    print("Distribution Grid Simulation Starting...")
    
    # Load profiles
    base_load, pv_gen, battery_specs = load_profiles()
    print(f"Loaded {len(base_load)} hours of data")
    
    # Calculate net load
    net_load = calculate_net_load(base_load, pv_gen)
    print(f"Net load range: {net_load.min():.2f} to {net_load.max():.2f} kW")

if __name__ == "__main__":
    main()

