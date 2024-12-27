import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd 
from sklearn.compose import ColumnTransformer
from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler,FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os 

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class Datatransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            replace_na_with_nan = lambda X: np.where(X=='na',np.nan,X)

            nan_replacement_step = ('nan_replacement',FunctionTransformer(replace_na_with_nan))
            imputer_step = ('imputer',SimpleImputer(strategy='constant',fill_value=0))
            scaler_step = ('scaler',RobustScaler())

            preprocessor = Pipeline(
                steps=[nan_replacement_step,imputer_step,
                       scaler_step]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
