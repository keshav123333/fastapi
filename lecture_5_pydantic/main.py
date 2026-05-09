from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated


class User(BaseModel):
    name:str
    weight:float
    height:float=16.5   #default value set ki hai 
    feedback:Optional[List[str]]=None   #default set tab bhi chalega bas optional m node likh sakta 
    metadata:Dict[str, str]
    email:EmailStr
    website:AnyUrl


def patentdata(patient:User):
    print(patient.name)
    print(patient.weight)
    print(patient.height)
    print(patient.feedback)
    print(patient.metadata)
    print(patient.email)
    print(patient.website)


patient={
    "name":"John Doe",
    "weight":70.5,
     
   
    "metadata":{"id": "12345", "created_at": "2023-01-01"},
    "email":"abc@example.com",
    "website":"https://www.example.com"

}

patient_para=User(**patient)
patentdata(patient_para)



