# ⚡ Distribution Grid Day-Ahead Simulation

<div align="center">

**A Python-based simulation framework for modeling distribution grid operations with renewable energy sources and battery storage**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Overview](#-overview) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Results](#-results) • [Technical Details](#-technical-details)

</div>

---

## 🎯 Overview

This project implements a **day-ahead simulation sandbox** for a small distribution feeder, demonstrating the integration and optimization of distributed energy resources (DER) in modern power grids. The simulation models the complex interactions between base load, renewable generation, and battery storage systems to achieve peak demand reduction and congestion management.

### What This Demonstrates

This simulation showcases capabilities directly applicable to **predictive congestion management** and **grid optimization**:

- **RES Integration Modeling:** Accurate representation of rooftop PV generation patterns and their impact on net load
- **DER Coordination:** Intelligent battery control algorithms for peak shaving and load smoothing
- **Congestion Quantification:** Novel metrics for measuring grid stress and infrastructure utilization
- **Predictive Analytics:** Day-ahead optimization strategies for reducing peak demand and operational costs

---

## ✨ Features

### 🔋 **Battery Energy Storage System (BESS)**
- 10 kWh capacity with 5 kW maximum power rating
- Bidirectional charging/discharging with efficiency modeling
- State-of-charge (SOC) tracking and constraint enforcement
- Intelligent control algorithms for peak shaving

### ☀️ **Renewable Energy Integration**
- Realistic rooftop PV generation profiles
- Time-series modeling of solar irradiance patterns
- Net load calculation accounting for variable generation

### 📊 **Advanced Analytics**
- Peak demand reduction quantification
- Congestion proxy metrics (sum of squared power flows)
- Comprehensive visualization of grid operations
- CSV export for further analysis

### 🎨 **Visualization & Reporting**
- Multi-panel plots showing load, generation, and battery operation
- Dual-axis charts for power flows and battery SOC
- High-resolution output suitable for presentations

---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hassan-Abidi/grid-simulation.git
   cd grid-simulation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python3 simulate_grid.py --help
   ```

---

## 💻 Usage

### Running the Simulation

Execute the main simulation script:

```bash
python3 simulate_grid.py
```

### Output Files

The simulation generates two key outputs:

1. **`simulation_results.png`** - Comprehensive visualization of the 24-hour simulation
2. **`simulation_results.csv`** - Detailed hourly data for further analysis

### Customizing Profiles

To modify load or generation profiles, edit the CSV files in the `profiles/` directory:

- `base_load.csv` - Hourly load demand (kW)
- `pv_generation.csv` - Hourly PV generation (kW)
- `battery_specs.csv` - Battery system parameters

---

## 📈 Results

### Performance Metrics

The simulation demonstrates significant benefits from intelligent battery control:

| Metric | Baseline (No Battery) | With Battery Control | Improvement |
|--------|----------------------|---------------------|-------------|
| **Peak Power Demand** | 8.50 kW | 6.00 kW | **↓ 29.4%** |
| **Congestion Proxy** | 359.00 | 281.62 | **↓ 21.6%** |

### Visualization

![Simulation Results](simulation_results.png)

The visualization shows three key aspects:

1. **Top Panel:** Base load, PV generation, and resulting net load profiles
2. **Middle Panel:** Battery charging/discharging behavior throughout the day
3. **Bottom Panel:** Final grid power demand and battery state of charge

### Key Insights

- **Morning Charging:** Battery charges during low-load periods (midnight to 6 AM) when grid capacity is available
- **Peak Shaving:** Battery discharges during evening peak (6-9 PM) to reduce maximum grid demand
- **PV Coordination:** Battery absorbs excess solar generation during midday, preventing reverse power flow
- **Congestion Relief:** Smoother power flows reduce stress on distribution infrastructure

---

## 🔬 Technical Details

### System Architecture

The simulation follows a modular architecture:

```
simulate_grid.py          # Main simulation engine
├── load_profiles()       # CSV data ingestion
├── calculate_net_load()  # Load-generation balance
├── initialize_battery()  # BESS initialization
├── battery_control()     # Peak-shaving algorithm
└── plot_results()        # Visualization generation
```

### Battery Control Algorithm

The control strategy implements a **threshold-based peak shaving** approach:

- **Discharge Mode:** When net load exceeds 6.0 kW, battery discharges to reduce grid demand
- **Charge Mode:** When net load falls below 2.0 kW, battery charges to store energy
- **Constraints:** All operations respect battery power limits and SOC boundaries

### Congestion Proxy Metric

The congestion proxy is calculated as:

```
Congestion = Σ(P_grid[t]²) for t = 0 to 23
```

This metric penalizes high power flows quadratically, making it sensitive to peak demands that stress grid infrastructure.

---

## 🛠️ Technology Stack

- **Python 3.11** - Core simulation engine
- **NumPy** - Numerical computations and array operations
- **Pandas** - Time-series data management
- **Matplotlib** - Scientific visualization

---

## 📊 Use Cases

This simulation framework is applicable to:

- **Grid Planning:** Evaluating DER integration scenarios for distribution system upgrades
- **Congestion Management:** Quantifying benefits of battery storage for peak reduction
- **Renewable Integration:** Analyzing PV hosting capacity and curtailment requirements
- **Market Design:** Modeling flexibility services and demand response programs
- **Research & Education:** Teaching power systems concepts and optimization techniques

---

## 🎓 Academic Context

This project demonstrates competencies relevant to:

- Distribution system modeling and analysis
- Renewable energy integration challenges
- Energy storage optimization
- Predictive congestion management
- Data-driven grid operations

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Hassan Abidi**

Developed as a demonstration of grid modeling and optimization capabilities for research assistant positions in power systems and renewable energy integration.

---

## 🙏 Acknowledgments

- Profile data based on typical residential load patterns and solar irradiance curves
- Simulation methodology inspired by industry best practices in distribution system operations
- Visualization design follows academic publication standards

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

</div>

