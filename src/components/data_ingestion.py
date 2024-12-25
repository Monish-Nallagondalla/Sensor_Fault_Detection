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
    train_data_path : str = os.path.join ('artufacts", "train.csv')
    
