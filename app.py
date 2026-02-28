from src.placement_prediction.looger import logging
from src.placement_prediction.exception import Cu_Exception
from src.placement_prediction.components.data_ingestion import Data_Ingestion
import pandas as pd
import sys
if __name__=="__main__":
    try:
        with open("artifacts/raw_data.csv","r") as f:
            df=pd.read_csv(f)
        
        print(df.head())
        df.drop(["student_id","gender","coding_skill_score","aptitude_score","communication_skill_score","logical_reasoning_score","hackathons_participated","github_repos","linkedin_connections","mock_interview_score","attendance_percentage","attendance_percentage","backlogs","extracurricular_score","leadership_score","volunteer_experience","sleep_hours","study_hours_per_day"],axis=1,inplace=True)
        print(df.columns)

    except Exception as e:
        raise Cu_Exception(e,sys)



 #   Column                     Non-Null Count   Dtype  
---  ------                     --------------   -----  
 0   age                        100000 non-null  int64  
 1   cgpa                       100000 non-null  float64
 2   branch                     100000 non-null  str    
 3   college_tier               100000 non-null  str    
 4   internships_count          100000 non-null  int64  
 5   projects_count             100000 non-null  int64  
 6   certifications_count       100000 non-null  int64  
 7   communication_skill_score  100000 non-null  float64
 8   backlogs                   100000 non-null  int64  
 9   placement_status           100000 non-null  str    
 10  salary_package_lpa         100000 non-null  float64