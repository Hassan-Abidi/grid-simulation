# Distribution Grid Day-Ahead Simulation

A Python-based simulation sandbox for modeling a small distribution grid with renewable energy sources and distributed energy resources.

## Goal

The primary goal of this project is to simulate 24 hours of operation for a small distribution feeder with three main components:

1.  **Base Load:** A typical residential load profile.
2.  **Rooftop PV:** A solar generation profile representing a sunny day.
3.  **Battery Storage:** A simple battery energy storage system (BESS).

The simulation computes the net load at each hour and applies a basic control algorithm to charge or discharge the battery, aiming to reduce the peak power drawn from the grid.

## What This Shows

This simulation demonstrates the ability to model the interaction between renewable energy sources (RES) and distributed energy resources (DER) in a simplified grid environment. By implementing a basic peak-shaving strategy, the project quantifies the benefits of battery storage in two key areas:

1.  **Peak Reduction:** The simulation shows a significant reduction in the peak power demand from the grid, which is a critical factor in grid stability and cost management.
2.  **Congestion Management:** A simple congestion proxy (sum of squared power flows) is used to illustrate how battery storage can alleviate stress on the grid infrastructure. A lower value indicates smoother power flows and reduced congestion.

These capabilities are a direct fit for predictive congestion management, as they provide a framework for forecasting grid conditions and optimizing DER to maintain stability.

## How to Run

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the simulation:**

    ```bash
    python3 simulate_grid.py
    ```

This will generate two output files:

*   `simulation_results.png`: A plot visualizing the simulation results.
*   `simulation_results.csv`: A CSV file containing the detailed hourly data.

## Simulation Results

![Simulation Results](simulation_results.png)

### Key Metrics

| Metric                 | Baseline | With Battery | Reduction | Percent Change |
| ---------------------- | -------- | ------------ | --------- | -------------- |
| Peak Power (kW)        | 8.50     | 6.00         | 2.50      | 29.4%          |
| Congestion Proxy       | 359.00   | 281.62       | 77.38     | 21.6%          |

As shown in the results, the battery successfully reduces the peak grid power by **29.4%** and the congestion proxy by **21.6%** under this simple control strategy.

