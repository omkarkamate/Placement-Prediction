from datetime import datetime
import logging
import os

path_dir=os.path.join(os.getcwd(), "logs")
os.makedirs(path_dir, exist_ok=True)

file_name = f"{datetime.now().strftime('%H-%M-%S_%d-%m-%Y')}.log"

logging.basicConfig(
    filename=os.path.join(path_dir, file_name),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)