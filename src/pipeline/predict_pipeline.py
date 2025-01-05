import shutil
import os,sys
import pandas as pd
from src.logger import logging

from src.exception import CustomException
from flask import request
from src.constant import *
from src.utils import download_model,load_object

from dataclasses import dataclass

@dataclass

class PredictionFileDetail:
    prediction_output_dirname: str = 'predictions'
    prediction_file_name: str ='predicted_file.csv'
    prediction_file_path : str = os.path.join(prediction_output_dirname,prediction_file_name)

class PredictionPipeline:
    def __init__(self,request:request):

        self.request = request 
        self.prediction_file_detail = PredictionFileDetail()

    def save_input_files(self)-> str:

        try:
            pred_file_input_dir = 'prediction_artifacts'
            os.makedirs(pred_file_input_dir,exist_ok=True)

            input_csv_file = self.request.files['file']
            pred_file_path = os.path.join(pred_file_input_dir,input_csv_file.filename)

            input_csv_file.save(pred_file_path)

            return pred_file_path
        except Exception as e:
            raise CustomException(e,sys)
        

    def predict(self,features):
        try: 
            model_path = download_model(
                bucket_name=AWS_S3_BUCKET_NAME,
                bucket_file_name='model.pkl'
                dest_file_name='model.pkl'
            )

            model = load_object(file_path=model_path)

            preds = model.predict(features)

            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        

    def get_predicted_dataframe(Self,input_dataframe_path:pd.DataFrame):

        try:
            prediction_column_name : str = "class"





