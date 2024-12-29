import os 
import sys
from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier,GradientboostingClassifier,Adaboostclassifier 
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.constant import * 
from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_models , load_object , save_object , upload_file 

@dataclass

class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class CustomModel:
    def __init__(self,X):
        transformed_feature = self.preprocessing_object.transform(X)

        return self.trained_model_object.predict(transformed_feature)
    
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"
    
    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"
    

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    