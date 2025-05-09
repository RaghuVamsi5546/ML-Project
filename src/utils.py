import os
import sys

import dill
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging


def save_object(file_path: str, obj: object) -> None:
    """
    Saves a Python object to a file using dill.

    Args:
        file_path (str): Path where the object will be saved.
        obj (object): Python object to be serialized.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        logging.info(f"Saving object to {file_path}")

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(f"Error saving object to {file_path}", sys) from e
