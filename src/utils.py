import os
import sys 

import boto3
import dill
import numpy as np
import pandas as pd 

from pymongo import MongoClient

from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.exception import CustomException


def export_collection_as_dataframe(collection_name,db_name):
    try :
        mongo_client = MongoClient(os.getenv("Mmongodb+srv://nsmonish:Monish1996@sensor-fault-detection.1il9p.mongodb.net/?retryWrites=true&w=majority&appName=Sensor-fault-detection"))

        collection = mongo_client[db_name][collection_name]

        df =pd.DataFrame(list(collection.find()))


        if "_id" in df.columns.to_list():
            df = df.drop(columns=['_id'],axis=1) 

            df.replace({'na':np.nan},inplace=True)

            return df
    except Exception as e:
        raise CustomException(e,sys)
    
'''By default, MongoDB includes an _id field in every document. This line checks if _id exists in the DataFrame's columns and drops it (if it exists), as it's often not required for analysis.'''
    


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException (e,sys)

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)

def u