 

from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from user_schema.user_schema import UserInput
from model.predict import predict_risk,MODEL_VERSION,_model
from user_schema.response_schema import PredictionResponse
import pandas as pd
import json 



app=FastAPI()





@app.get("/")
def home():
    return {"working": True}

# YE API ROUTE KUBERNETE AND ALL KE LIYE ISSE VO CHCK KI KYA SAHI KAAM KAR RAHA 
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": _model is not None,
        "model_version": MODEL_VERSION
    }




@app.post("/predict")
def predict_risk(data: UserInput,response_model=PredictionResponse):
   #yaha upar response model = prediction response se specify kr skta hu ki response kis format m chahiye ye apne aap verify 
     
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    try:
        pred=predict_risk(input_df)
        #yaha pe response kiss forma m ye bhi sepcfy kar skata 

        return JSONResponse(status_code=200, content=pred)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")