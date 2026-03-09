from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
from src.placement_prediction.components.data_preprocessing import Data_preprocessing
import pandas as pd
import sys
if __name__=="__main__":
    try:
        # with open("artifacts/raw_data.csv","r") as f:
        #     df=pd.read_csv(f)
        
        # print(df.head())
        # df.drop(["student_id","gender","coding_skill_score","aptitude_score","communication_skill_score","logical_reasoning_score","hackathons_participated","github_repos","linkedin_connections","mock_interview_score","attendance_percentage","attendance_percentage","backlogs","extracurricular_score","leadership_score","volunteer_experience","sleep_hours","study_hours_per_day"],axis=1,inplace=True)
        # print(df.columns)

        obj=Data_preprocessing()
        print(obj.Data_Preprocess("artifacts/train_data.csv","artifacts/test_data.csv"))
        


    except Exception as e:
        raise Cu_Exception(e,sys)
