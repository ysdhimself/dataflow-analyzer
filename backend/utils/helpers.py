# utils/helpers.py
from pydantic import BaseModel, ValidationError
from typing import List

class TrainSchema(BaseModel):
    series: List[List[float]]

class DetectSchema(BaseModel):
    point: List[float]

def validate_train(data):
    try:
        validated = TrainSchema(**data)
        return validated.series, None
    except ValidationError as e:
        return None, e.errors()

def validate_detect(data):
    try:
        validated = DetectSchema(**data)
        return validated.point, None
    except ValidationError as e:
        return None, e.errors()
