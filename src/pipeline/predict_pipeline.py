import shutil
import os
import sys
import pandas as pd
from flask import request
from src.logger import logging
from src.exception import CustomException
from src.constant import *
from src.utils import download_model, load_object
from dataclasses import dataclass

@dataclass
class PredictionFileDetail:
    prediction_output_dirname: str = 'predictions'
    prediction_file_name: str = 'predicted_file.csv'
    prediction_file_path: str = os.path.join(prediction_output_dirname, prediction_file_name)

class PredictionPipeline:
    def __init__(self, request: request): # type: ignore
        self.request = request
        self.prediction_file_detail = PredictionFileDetail()

    def save_input_files(self) -> str:
        try:
            pred_file_input_dir = "prediction_artifacts"
            # Ensure the directory exists before attempting to save the file
            if not os.path.exists(pred_file_input_dir):
                os.makedirs(pred_file_input_dir)

            input_csv_file = self.request.files['file']
            pred_file_path = os.path.join(pred_file_input_dir, input_csv_file.filename)
            
            # Save the file to the correct location
            input_csv_file.save(pred_file_path)

            return pred_file_path
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try: 
            model_path = download_model(
                bucket_name=AWS_S3_BUCKET_NAME,
                bucket_file_name='model.pkl',
                dest_file_name='model.pkl'
            )

            model = load_object(file_path=model_path)

            preds = model.predict(features)

            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

    def get_predicted_dataframe(self, input_dataframe_path: pd.DataFrame):
        try:
            prediction_column_name: str = "class"
            input_dataframe: pd.DataFrame = pd.read_csv(input_dataframe_path)

            predictions = self.predict(input_dataframe)
            input_dataframe[prediction_column_name] = [pred for pred in predictions]

            target_column_mapping = {0: 'neg', 1: 'pos'}
            input_dataframe[prediction_column_name] = input_dataframe[prediction_column_name].map(target_column_mapping)
            
            # Ensure the output directory exists before saving predictions
            if not os.path.exists(self.prediction_file_detail.prediction_output_dirname):
                os.makedirs(self.prediction_file_detail.prediction_output_dirname)

            input_dataframe.to_csv(self.prediction_file_detail.prediction_file_path, index=False)
            logging.info("Predictions completed.")

        except Exception as e:
            raise CustomException(e, sys) from e

    def run_pipeline(self):
        try:
            input_csv_path = self.save_input_files()
            self.get_predicted_dataframe(input_csv_path)

            return self.prediction_file_detail
        
        except Exception as e:
            raise CustomException(e, sys)
