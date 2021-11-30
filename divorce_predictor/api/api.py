#!/usr/bin/env python
from pathlib import Path
from typing import Any, List

import pandas as pd
from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel


class Item(BaseModel):
    Atr1: List[int]
    Atr2: List[int]
    Atr3: List[int]
    Atr4: List[int]
    Atr5: List[int]
    Atr6: List[int]
    Atr7: List[int]
    Atr8: List[int]
    Atr9: List[int]
    Atr10: List[int]
    Atr11: List[int]
    Atr12: List[int]
    Atr13: List[int]
    Atr14: List[int]
    Atr15: List[int]
    Atr16: List[int]
    Atr17: List[int]
    Atr18: List[int]
    Atr19: List[int]
    Atr20: List[int]
    Atr21: List[int]
    Atr22: List[int]
    Atr23: List[int]
    Atr24: List[int]
    Atr25: List[int]
    Atr26: List[int]
    Atr27: List[int]
    Atr28: List[int]
    Atr29: List[int]
    Atr30: List[int]
    Atr31: List[int]
    Atr32: List[int]
    Atr33: List[int]
    Atr34: List[int]
    Atr35: List[int]
    Atr36: List[int]
    Atr37: List[int]
    Atr38: List[int]
    Atr39: List[int]
    Atr40: List[int]
    Atr41: List[int]
    Atr42: List[int]
    Atr43: List[int]
    Atr44: List[int]
    Atr45: List[int]
    Atr46: List[int]
    Atr47: List[int]
    Atr48: List[int]
    Atr49: List[int]
    Atr50: List[int]
    Atr51: List[int]
    Atr52: List[int]
    Atr53: List[int]
    Atr54: List[int]


class PredictionResult(BaseModel):
    predictions: List[Any]


app = FastAPI()


@app.get("/")
async def root():
    return {"greetings": "Divorce Predictor here! Welcome!"}


@app.post("/estimator/predict")
async def predict(item: Item) -> PredictionResult:
    experiment_artifacts_folder = Path(__file__).parent.parent.parent / "ml" / "output"
    model_artifact_file = experiment_artifacts_folder / "estimator.joblib"

    estimator = load(model_artifact_file)
    df_to_predict = pd.DataFrame(item.dict()).values
    predictions = estimator.predict(df_to_predict).ravel().tolist()
    response = PredictionResult(**{"predictions": predictions})

    return response
