# uvicorn api:app --reload if tere app jaha pe application uska name api.py toh ye kar 

from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()

def load_json():
    with open("patient.json") as f:
        data =json.load(f)
    return data

@app.get("/")
def get_home():
    return {"hello world": "this is a simple fastapi application"}

@app.get("/patient")
def get_patient():
    data=load_json()
    return data

@app.get("/patient/{id}")
def get_patient_by_id(id:str=Path(...,description="the id of the patient you want to get",example="P10234",min_length=6,max_length=20)): 
    #isme aur cheeze bhi add kar sakte gt regex etc isse server ko idea ki kya chaiye and vo kitna bada ya chota ho jo param bhejenge 
#... teen dot mean ye important hai 
    data=load_json()

    if id in data.keys():
        return data[id]
    else :
        # return {"message":"patient not found"}   ye purana method no
        raise HTTPException(status_code=404,detail="patient not found")  # ye naya method hai fastapi ka jo ki error ko handle karta hai aur client ko proper response deta hai


@app.get("/patients/sort")
def get_patient_sorted(sortby:str=Query(...,description="the field by which you want to sort the patient data",example="height age bmi"),
                       order:str=Query(default="asc",description="the order in which you want to sort the patient data",example="asc desc")):
#    yaha maine order asc so ye ni bhi jaye url m toh dikkat ni and upar sortby ko main ... teen dot toh vo imp
    options=["height","age","bmi"]
    if sortby not in options:
        raise HTTPException(status_code=400,detail=f"invalid sortby value. must be one of {options}")
    
    data=load_json()
    # ord=True if order=="asc" else False   aise bhi bhej sakta yaha niche reverse meinreverse=ord likh dena 
    sorted_data=sorted(data.values(),key=lambda x:x[sortby],reverse=(order=="desc"))
    return sorted_data
