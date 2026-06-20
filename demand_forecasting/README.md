# Demand Forecasting Module

## Overview

This module predicts future electricity demand using an LSTM (Long Short-Term Memory) neural network.

## Dataset

UCI Individual Household Electric Power Consumption Dataset

## Model

* Model Type: LSTM
* Framework: TensorFlow / Keras
* Input: Historical power consumption values
* Output: Predicted future demand

## Features Used

* Global Active Power
* Global Reactive Power
* Voltage
* Global Intensity
* Sub Metering 1
* Sub Metering 2
* Sub Metering 3

## Files

* train_lstm.py → Model Training
* predict.py → Demand Prediction
* demand_lstm.keras → Saved Model

## Sample Output

Predicted Future Demand:
0.94 kW

## Future Enhancements

* Real-time Demand Forecasting
* Dashboard Integration
* Demand Trend Visualization
* API Integration
