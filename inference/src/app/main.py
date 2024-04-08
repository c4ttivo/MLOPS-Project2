from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from src.models.train import train



class Covertype(BaseModel):
    Cover_Type: int = 0
    Elevation: int = 0
    Hillshade_9am: int = 0
    Hillshade_Noon: int = 0
    Horizontal_Distance_To_Fire_Points: int = 0
    Horizontal_Distance_To_Hydrology: int = 0
    Horizontal_Distance_To_Roadways: int = 0
    Slope: int = 0
    Soil_Type: str = "C2702"
    Vertical_Distance_To_Hydrology: int = 0
    Wilderness_Area: str = "Cache"

    
app = FastAPI()

@app.get("/")
async def root():
    
    return {"message": "Convet Type Inference API"}

@app.post("/predict/")
def predict_species_random_forest(convertype: Covertype):
    # TODO

    return{"Predicted"}
