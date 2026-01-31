import os
from pathlib import Path
import logging
from typing import List


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{__name__}/__init__.py",
    f"src/{__name__}/components/__init__.py",
    f"src/{__name__}/utils/__init__.py",
    f"src/{__name__}/components/data_ingestion.py",  
    f"src/{__name__}/components/data_transformation.py",
    f"src/{__name__}/components/model_trainer.py",
    f"src/{__name__}/components/model_evaluation.py",
    f"src/{__name__}/exceptions.py",
    f"src/{__name__}/logger.py",
    f"src/{__name__}/utils/common.py",
    "app.py",
    "requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Created directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as fp:
            pass
        logger.info(f"Created empty file: {filepath}")
    
    else:
        logger.info(f"File already exists and is not empty: {filepath}")


def read_template(template_path: str) -> str:
    """Reads a template file and returns its content as a string."""
    if not os.path.exists(template_path):
        logger.error(f"Template file {template_path} does not exist.")
        raise FileNotFoundError(f"Template file {template_path} not found.")
    
    with open(template_path, 'r') as file:
        content = file.read()
        logger.info(f"Successfully read template from {template_path}")
        return content