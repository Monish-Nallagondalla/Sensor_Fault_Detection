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