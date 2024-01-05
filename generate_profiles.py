#!/usr/bin/env python3
"""
Generate CSV profiles for base load, PV generation, and battery capacity.
"""

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Time array: 24 hours
hours = np.arange(0, 24)

# Base load profile (kW)
# Typical residential load pattern
base_load = np.array([
    2.5, 2.2, 2.0, 1.8, 1.7, 2.0,  # 0-5: night/early morning
    3.5, 5.0, 6.5, 5.5, 4.5, 4.0,  # 6-11: morning peak
    4.2, 4.5, 4.3, 4.8, 6.0, 8.5,  # 12-17: afternoon
    9.0, 8.0, 6.5, 5.0, 4.0, 3.0   # 18-23: evening peak
])

# Save base load profile
df_load = pd.DataFrame({
    'hour': hours,
    'load_kw': base_load
})
df_load.to_csv('profiles/base_load.csv', index=False)
print("Generated base_load.csv")

# PV generation profile (kW)
# Solar generation follows typical bell curve during daylight hours
pv_generation = np.array([
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  # 0-5: no sun
    0.5, 1.5, 3.0, 4.5, 5.5, 6.0,  # 6-11: morning ramp
    6.2, 6.0, 5.5, 4.5, 3.0, 1.5,  # 12-17: afternoon decline
    0.5, 0.0, 0.0, 0.0, 0.0, 0.0   # 18-23: no sun
])

# Save PV generation profile
df_pv = pd.DataFrame({
    'hour': hours,
    'pv_kw': pv_generation
})
df_pv.to_csv('profiles/pv_generation.csv', index=False)
print("Generated pv_generation.csv")

# Battery specifications
battery_capacity_kwh = 10.0  # 10 kWh battery
battery_max_power_kw = 5.0   # 5 kW max charge/discharge rate

# Save battery specs
df_battery = pd.DataFrame({
    'parameter': ['capacity_kwh', 'max_power_kw'],
    'value': [battery_capacity_kwh, battery_max_power_kw]
})
df_battery.to_csv('profiles/battery_specs.csv', index=False)
print("Generated battery_specs.csv")

if __name__ == "__main__":
    pass

