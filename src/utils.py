import os
import sys

import dill
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score

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


def evaluate_models(X_train, X_test, y_train, y_test, models):
    try:
        report = {}

        report = {}
        for key, model in models.items():
            model.fit(X_train, y_train)


            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[key] =test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)