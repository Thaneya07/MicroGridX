# Solar Forecasting Module - MicroGridX

## Overview

This module predicts future solar energy generation using a Long Short-Term Memory (LSTM) neural network. Historical weather parameters such as temperature, humidity, wind speed, average wind speed, and atmospheric pressure are used to forecast solar power generation.

## Features

* Data preprocessing and cleaning
* Time-series sequence generation
* LSTM-based solar forecasting
* JSON-based output generation
* Integration-ready architecture

## Technology Stack

* Python
* TensorFlow / Keras
* Pandas
* NumPy
* Scikit-Learn

## Output

Example:

{
"timestamp": "2026-06-22T13:13:01",
"predicted_solar": 15389.96,
"model": "LSTM"
}

## Project Structure

data/
models/
preprocess.py
train_lstm.py
predict_solar.py
solar_output.json

## Author

MicroGridX Team
