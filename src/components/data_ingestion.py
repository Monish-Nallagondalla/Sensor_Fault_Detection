import os 
import sys 
from dataclasses import dataclass 

import pandas as pd
from sklearn.model_selection import train_test_split

from src.constant import *
from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join ('artifacts", "train.csv')
    raw_data_path : str = os.path.join ('artifacts','data.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered Inititaion_data_ingestion method of DataIngestion Class")

    try:
        df : pd.DataFrame = export_collection_as_dataframe(
            db_name =
        )