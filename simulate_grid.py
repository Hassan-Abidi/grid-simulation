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

def main():
    print("Distribution Grid Simulation Starting...")
    
    # Load profiles
    base_load, pv_gen, battery_specs = load_profiles()
    print(f"Loaded {len(base_load)} hours of data")

if __name__ == "__main__":
    main()

