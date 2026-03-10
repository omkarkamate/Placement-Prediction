from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
from src.placement_prediction.components.model_trainer import model_training
import pandas as pd
import sys
if __name__=="__main__":
    try:
        obj=model_training()
        print(obj.initiate_model_training("notebook/cleanDF.csv"))
        
        


    except Exception as e:
        raise Cu_Exception(e,sys)
