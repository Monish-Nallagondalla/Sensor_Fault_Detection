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
        mongo_client = MongoClient(os.getenv("M"))