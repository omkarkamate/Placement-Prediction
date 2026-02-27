from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
from src.placement_prediction.components.data_ingestion import Data_Ingestion
import sys
if __name__=="__main__":
    try:
        data_ingestion=Data_Ingestion()
        df=data_ingestion.initiate_data_ingestion()
        logging.info("Completed the data ingestion")
        print(df)

    except Exception as e:
        raise Cu_Exception(e,sys)