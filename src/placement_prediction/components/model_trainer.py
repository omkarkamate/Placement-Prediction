import pandas as pd
from dataclasses import dataclass
import os
import sys
from src.placement_prediction.exception import Cu_Exception
from src.placement_prediction.looger import logging
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,recall_score

@dataclass

class model_train_config:
    MTConfig=os.path.join("artifacts","model.pkl")

class model_training:
    def __init__(self):
        self.Config=model_train_config()
    
    def initiate_model_training(self,path):
        raw_df=pd.read_csv(path)
        # raw_df=raw_df.sample(500)
        raw_df["placement_status"] = raw_df["placement_status"].map({"Not Placed": 0,"Placed": 1})
        logging.info("Reading raw data")
        X=raw_df.drop(["placement_status"],axis=1)
        y=raw_df["placement_status"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
        logging.info("Split data into train test")

        with open("artifacts/Data_Preprocessing.pkl", "rb") as file:
            preprocessor = pickle.load(file)

        X_train=preprocessor.fit_transform(X_train)
        X_test=preprocessor.transform(X_test)
        logging.info("preprocessing data")

        models={
            "LogisticRegression":LogisticRegression(class_weight="balanced"),
            "Tree":DecisionTreeClassifier(),
            "svm":SVC(kernel="rbf"),
            "Random_Forest":RandomForestClassifier(n_estimators=100,random_state=42),
            "Naive_Bayes":GaussianNB(),
            "Ada":AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=6),n_estimators=500,learning_rate=0.3,random_state=42),
            "Gradient":GradientBoostingClassifier(n_estimators=500,max_depth=5,learning_rate=0.3,random_state=42),
            "XGBoost":XGBClassifier(n_estimators=500,max_depth=6,learning_rate=0.3,random_state=42,subsample=0.8,colsample_bytree=0.8,eval_metric="logloss"),
        }
        

        report={}


        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)
            y_test_pred=model.predict(X_test)
            acc_score=accuracy_score(y_test,y_test_pred)
            recall__score=recall_score(y_test,y_test_pred)

            # report[list(models.keys())[i]]=score

            report[list(models.keys())[i]] = {
                "accuracy": acc_score,
                "recall": recall__score
            }
        
        
    
        logging.info("applying various model ")

        best_model_name = max(report, key=lambda k: report[k]["accuracy"])
        best_model_score = report[best_model_name]["accuracy"]

        best_model = models[best_model_name]
        logging.info(f"selected best model which is {best_model_name}")

        with open(self.Config.MTConfig, "wb") as f:
            pickle.dump(best_model,f)
        
        print(report)
        
        return best_model_name,best_model_score





