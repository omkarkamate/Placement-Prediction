import os
from pathlib import Path

project_name="placement_prediction"

files=[
    "setup.py",
    "requirements.txt",
    "README.md",
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components.py/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/looger.py",
    f"src/{project_name}/exception.py",
    "app.py"
]

for file in files:
    file_dir,file_name = os.path.split(file)
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
    
    if not os.path.exists(file):
        with open(file,'w') as f:
            pass

