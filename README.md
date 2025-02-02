# Diamond Price Prediction

![Python](https://img.shields.io/badge/Language-Python-blue) ![MIT License](https://img.shields.io/badge/License-MIT-green)

## 1. 📜 Description
This project predicts diamond prices using machine learning models trained on a dataset containing various attributes of diamonds such as carat, cut, color, clarity, and other features. The goal is to predict the price of a diamond based on these features to aid buyers, sellers, and researchers in the diamond industry.

## 2. 🏗️ Project Structure
The repository is organized into logical modules for clarity and scalability:

### Core Components
- **`config/`**: Configuration files for model settings and data schema.
- **`src/`**: Source code for the application, including components for data handling and pipelines.
- **`notebooks/`**: Jupyter notebooks for exploration and modeling.

### Main Files
- **`application.py`**: Main application script to run the project.
- **`diamonds_data.csv`**: Dataset for training and evaluation.
- **`requirements.txt`**: Python dependencies.
- **`setup.py`**: Setup script for package installation.
- **`LICENSE`**: Licensing information.
- **`README.md`**: Documentation file (this file).

### Detailed Project Structure:

```plaintext
Diamond_price_prediction/
│
├── config/               # Configuration files
│   ├── model.yaml        # Model hyperparameters and settings
│   └── schema.yaml       # Data schema specifications
│
├── notebooks/            # Jupyter notebooks for exploration and modeling
│   ├── diamondPrice.ipynb
│   └── eda.ipynb
│
├── src/                  # Source code for the application
│   ├── components/       # Core components for data handling and modeling
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipelines/        # Training and prediction pipelines
│   │   ├── __init__.py
│   │   ├── prediction_pipeline.py
│   │   └── training_pipeline.py
│   ├── exception.py      # Custom error handling
│   ├── logger.py         # Logging utility
│   └── utils.py          # Helper functions
│
├── application.py        # Main application script
├── diamonds_data.csv     # Dataset for training and evaluation
├── LICENSE               # Licensing information
├── requirements.txt      # Python dependencies
├── setup.py              # Setup script for package installation
└── README.md             # Documentation (this file)
```

## 3.  📊 Dataset Overview
The dataset contains various features of diamonds such as their size, color, clarity, and price.

Key features:
- **Carat**: Weight of the diamond.
- **Cut**: Quality of the cut (Fair, Good, Very Good, Ideal, Excellent).
- **Color**: Diamond color, from D (best) to J (worst).
- **Clarity**: Diamond clarity rating (I1, SI1, SI2, VS1, VS2, VVS1, VVS2, IF).
- **Depth**: Depth percentage.
- **Table**: Table percentage.
- **Price**: Target variable, representing the price of the diamond.

Sample data:
| Carat | Cut    | Color | Clarity | Depth | Table | Price |
|-------|--------|-------|---------|-------|-------|-------|
| 0.23  | Ideal  | E     | SI2     | 61.5  | 55    | 326   |

## 4.  🚀 Features
- **Data Analysis**: Comprehensive exploratory data analysis (EDA) to identify patterns and relationships.
- **Model Training**: Machine learning pipelines to predict diamond price.
- **Web Application**: An intuitive interface for data input and predictions.
- **Customizable Configurations**: YAML-based configurations for models and data schema.

## 5.  ⚙️ Installation
### Prerequisites
- Python 3.8 or later
- Libraries specified in `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Monish-Nallagondalla/Diamond_price_prediction.git
   cd Diamond_price_prediction
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
   python application.py
   ```
2. Open your browser and navigate to `http://localhost:5000`.

### Notebooks
- Analyze data trends in `notebooks/eda.ipynb`.
- Train and evaluate models using `notebooks/diamondPrice.ipynb`.

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
```
