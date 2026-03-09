from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
import pandas as pd
import os
import sys
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pickle
import numpy as np



df=pd.read_csv("artifacts/raw_data.csv")

class Data_Preprocessing_Config:
    DPConfig=os.path.join("artifacts","Data_Preprocessing.pkl")
    logging.info("Data Preprocessing config created")

class Data_preprocessing:
    def __init__(self):
        self.Config=Data_Preprocessing_Config()
    
    def initiate_data_Preprocesiing(self):
        try:

            num_columns=["age","cgpa","internships_count","projects_count","certifications_count","communication_skill_score","backlogs"]
            cat_columns=["branch","college_tier"]

           

            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="mean")),
                ("scaler",StandardScaler())
            ])

            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("Encoding",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])


            preprocessor=ColumnTransformer([
                ("num",num_pipeline,num_columns),
                ("cat",cat_pipeline,cat_columns)

            ])

            return preprocessor

        except(Exception) as e:
            raise Cu_Exception(e,sys)
        
    def Data_Preprocess(self,train_path,test_path):
        try:
            
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)

            preprocessor=self.initiate_data_Preprocesiing()

            X_train=train_data.drop(columns=["placement_status","salary_package_lpa"])
            y_train=train_data["placement_status"]
            X_test=test_data.drop(columns=["placement_status","salary_package_lpa"])
            y_test=test_data["placement_status"]

            logging.info("data split in target columns")

            X_train=preprocessor.fit_transform(X_train)
            X_test=preprocessor.transform(X_test)

            logging.info("preprocessing on train test data")

            train_data=np.c_[X_train,np.array(y_train)]
            test_data=np.c_[X_test,np.array(y_test)]

            with open(self.Config.DPConfig,"wb") as f:
                pickle.dump(preprocessor,f)

            logging.info("pickle file created")

            return train_data,test_data
        



        except(Exception) as e:
            raise Cu_Exception(e,sys)