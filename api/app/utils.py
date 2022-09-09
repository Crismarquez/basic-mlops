from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
import pandas as pd
import os
from io import BytesIO
from config.config import MODELS_DIR

def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH','store/models/model.pkl')

    with open(model_path, 'rb') as model_file:
        model = load(BytesIO(model_file.read()))

    return model

def transform_to_dataframe(class_model: BaseModel) -> pd.DataFrame:
    transition_dictionary = {key: [value] for key, value in class_model.dict().items()}
    data_frame = pd.DataFrame(transition_dictionary)
    return data_frame