
```
# Wafer Fault Detection

## Overview
This project focuses on predicting faulty wafers in a photovoltaic power generation system using machine learning. Wafers are essential components in solar cell manufacturing, and detecting faults in these wafers can significantly reduce operational disruptions and costs. The goal of this project is to predict whether a wafer is faulty or not based on sensor data, thereby automating the process and minimizing human intervention.

## Problem Statement
Wafers are located at remote locations and contain hundreds of sensors that collect data continuously. These sensors measure various parameters, and the aim is to determine if a wafer is faulty using this sensor data. Detecting faulty wafers manually is time-consuming, labor-intensive, and costly, especially when false negatives occur. By applying machine learning, we can predict faults and avoid unnecessary operations, reducing downtime and increasing operational efficiency.

## Data
The dataset consists of sensor readings from multiple wafers. The data includes 400+ sensors, with each sensor providing a unique value. The task is to predict whether the wafer is faulty (`Good` or `Bad`) based on the sensor readings.

Sample data format:
| Sensor-1 | Sensor-2 | Sensor-3 | ... | Sensor-400 | Fault Status |
|----------|----------|----------|-----|------------|--------------|
| 2968.33  | 2476.58  | 2216.73  | ... | 0.9215     | Good         |
| 2021.33  | 1500.12  | 2317.22  | ... | 0.9235     | Bad          |

## Project Structure

```
wafer_fault_detection/
│
├── data/                  # Directory for the raw dataset
│   └── wafer_data.csv     # Sample dataset file
│
├── src/                   # Source code for data processing and model training
│   ├── data_processing.py # Script for data loading and preprocessing
│   ├── model.py           # Script for machine learning model creation and evaluation
│   └── utils.py           # Helper functions for various tasks
│
├── notebooks/             # Jupyter notebooks for analysis and experimentation
│   └── wafer_model.ipynb  # Notebook for exploratory data analysis and model training
│
├── requirements.txt       # Python package dependencies
├── README.md              # Project description and instructions
└── LICENSE                # Project license
```

## Installation

To set up this project, follow the instructions below:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wafer-fault-detection.git
   cd wafer-fault-detection
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Jupyter notebook for exploratory data analysis and model training:
   ```bash
   jupyter notebook notebooks/wafer_model.ipynb
   ```

## Usage

- **Data Processing**: The `data_processing.py` script can be used to load and preprocess the dataset. It includes functions for handling missing values, normalizing data, and splitting it into training and test sets.
  
- **Model Training**: The `model.py` script contains the machine learning model. It allows you to train a model, evaluate its performance, and save the trained model for future use.

- **Evaluation**: The model's performance is evaluated using common metrics such as accuracy, precision, recall, and F1-score. The trained model can be used to predict faulty wafers on unseen data.

## Model

The machine learning model used for wafer fault detection is a **classification model**. We aim to classify wafers as either `Good` or `Bad` based on sensor readings.

Model performance is evaluated based on:

- Accuracy
- Precision
- Recall
- F1-Score

## Future Work

- **Model Improvement**: Explore other machine learning algorithms such as Random Forest, Gradient Boosting, and Neural Networks for better prediction accuracy.
- **Real-Time Prediction**: Implement a real-time prediction system where data from sensors can be passed into the model, and predictions are made instantly.
- **Data Augmentation**: Generate synthetic data to enhance the model's robustness.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
