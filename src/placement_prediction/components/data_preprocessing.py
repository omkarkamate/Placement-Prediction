import pandas as pd
from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
import sys
import os
import pickle


class data_transformation_congig:
    config_path=os.path.join("artifacts,preprocessing.pkl")

class data_preprocessing:
    def __init__(self):
        self.config=data_transformation_congig.config_path()
    
    def initiate_preprocessing(self):
        

    