import pandas as pd
from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
import os
import sys
from sklearn.model_selection import train_test_split   

class Data_Ingestion_Config:
    config=os.path.join("artifacts","raw_data.csv")

class Data_Ingestion:
    def __init__(self):
        self.ingestion_config=Data_Ingestion_Config()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df=pd.read_csv(r"E:\dataset\student_placement_prediction_dataset_2026.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.config),exist_ok=True)

            df.to_csv(self.ingestion_config.config,index=False)
            logging.info("Exported the data to csv file")

            train_df,test_df=train_test_split(df,test_size=0.2,random_state=42)

            train_df.to_csv(os.path.join("artifacts","train_data.csv"),index=False)
            test_df.to_csv(os.path.join("artifacts","test_data.csv"),index=False)

            return df.head()

        except Exception as e:
            raise Cu_Exception(e,sys)
