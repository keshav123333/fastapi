from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse

from pydantic import BaseModel,computed_field,Field
import json

app=FastAPI()
# "name": "Neha Sinha", "city": "Kolkata", "age": 30, "gender": "female", "height": 1.55, "weight": 75, "bmi": 31.22, "verdict": "Obese"}}
class Patient(BaseModel):
    id:str
    name:str
    age:int
    city:str
    gender:str
    height:float
    weight:int

    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def verdict(self)->str:
        bmi=self.bmi
        if bmi<18.5:
            return "Underweight"
        elif 18.5<=bmi<25:
            return "Normal weight"
        elif 25<=bmi<30:
            return "Overweight"
        else:
            return "Obese"




def load_json():
    with open("data.json") as f:
        data=json.load(f)
    return data


def save_json(data):
    with open("data.json","w") as f:
        json.dump(data,f,indent=4)


@app.get("/")
def read_root():
    return {"message":"Hello World"}


@app.post("/patients")
def create_patient(patient:Patient):
    data=load_json()

    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient with this ID already exists")
    data[patient.id] = patient.model_dump(exclude={"id"})
    save_json(data)
    return JSONResponse(content={"message":"Patient created successfully"},status_code=201)
