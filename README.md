# Sensor Fault Detection

![Python](https://img.shields.io/badge/Language-Python-blue) ![MIT License](https://img.shields.io/badge/License-MIT-green)

## 1. 📜 Description
This project focuses on detecting faults in sensor data collected from industrial equipment. Using machine learning techniques, the project identifies faulty sensor readings and provides insights into sensor health, allowing for proactive maintenance and improved operational efficiency.

## 2. 🏗️ Project Structure
The repository is organized into logical modules for clarity and scalability:

### Core Components
- **`config/`**: Configuration files for model settings and data schema.
- **`src/`**: Source code for the application, including components for data handling and pipelines.
- **`templates/`**: HTML templates for the web app.

### Main Files
- **`app.py`**: Main application script to run the project.
- **`wafer_23012020_041211.csv`**: Dataset for training and evaluation.
- **`requirements.txt`**: Python dependencies.
- **`setup.py`**: Setup script for package installation.
- **`LICENSE`**: Licensing information.
- **`README.md`**: Documentation file (this file).

### Detailed Project Structure:

```plaintext
Sensor_fault_detection/
│
├── notebooks/            # Jupyter notebooks for exploration and modeling
│   ├── EDA.ipynb         # Exploratory Data Analysis
│   ├── upload.ipynb      # Upload data for processing
│
├── src/                  # Source code for the application
│   ├── __pycache/        # Cached Python files
│   ├── components/       # Core components for data handling and modeling
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── constant/         # Constants used across the project
│   │   └── __init__.py
│   ├── pipeline/         # Training and prediction pipelines
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py      # Custom error handling
│   ├── logger.py         # Logging utility
│   └── utils.py          # Helper functions
│
├── static/               # Static files for the web app
│   └── css/              # Stylesheets
│
├── templates/            # HTML templates for the web app
│   ├── upload_file.html  # File upload interface
│
├── app.py                # Main application script
├── wafer_23012020_041211.csv # Dataset for training and evaluation
├── LICENSE               # Licensing information
├── requirements.txt      # Python dependencies
├── setup.py              # Setup script for package installation
├── .gitignore            # Git ignore file
└── README.md             # Documentation (this file)
```

## 3. 📊 Dataset Overview
The dataset consists of sensor readings, each tagged with a status indicating whether the sensor is working properly or has faults.  
Key features:
- **Sensor ID**: Unique identifier for each sensor.
- **Sensor Type**: The type of sensor used (e.g., temperature, pressure).
- **Reading Value**: The sensor's output at the given time.
- **Timestamp**: Date and time the reading was recorded.
- **Fault Status**: Binary target variable indicating whether a fault is present (1) or not (0).

Sample data:
| Sensor ID | Sensor Type | Reading Value | Timestamp           | Fault Status |
|-----------|-------------|---------------|---------------------|--------------|
| 101       | Temperature | 75.5          | 2024-01-10 12:00:00 | 0            |
| 102       | Pressure    | 2.3           | 2024-01-10 12:05:00 | 1            |

## 4. 🚀 Features
- **Fault Detection**: Machine learning models for identifying sensor faults.
- **Data Analysis**: In-depth exploratory data analysis (EDA) to understand sensor behavior.
- **Model Training**: Custom pipelines for training fault detection models.
- **Web Application**: A user-friendly interface to upload sensor data and receive predictions.
- **Customizable Configurations**: YAML-based configurations for models and data schema.

## 5. ⚙️ Installation
### Prerequisites
- Python 3.8 or later
- Libraries specified in `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Monish-Nallagondalla/Sensor_fault_detection.git
   cd Sensor_fault_detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the project:
   ```bash
   python setup.py install
   ```

## 6. 📂 Usage
### Running the Application
1. Execute the main application script:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:5000`.

### Notebooks
- Explore sensor data trends in `notebooks/EDA.ipynb`.
- Upload data for processing using `notebooks/upload.ipynb`.

## 7. 🤝 Contributing
We welcome contributions! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed descriptions.

## 8. 📝 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

## 9. 📬 Contact
For questions or feedback:
- **GitHub**: [Monish-Nallagondalla](https://github.com/Monish-Nallagondalla)
- **Email**: [nsmonish@gmail.com]

---
