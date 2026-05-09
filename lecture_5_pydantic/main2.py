from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated


class User(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Type the name of the patient",description="type full name of the patient ",
    json_schema_extra={'example': ["keshav rai","Nitish rajput"]})]
    weight:Annotated[float,Field(gt=10,lt=100)]
    height:Annotated[float,Field(default=16.7,strict=True)]  #default value set ki hai  ans strict ko true as pydantic m "12.6" aise toh isse string kar leta but m ni toh iss true ab vo error throw if string m no. pass
    feedback:Optional[List[str]]=None   #default set tab bhi chalega bas optional m node likh sakta 
    metadata:Dict[str, str]
    age:Annotated[int,Field(gt=0,lt=150)]
    contacts:Dict[str,int]
    email:EmailStr
    website:AnyUrl

    #we use filed validator to check any condition on single field
    @field_validator('email') 
    @classmethod
    def email_validator(cls,value): #Yaha pe mode after set hota hai 
        valid=["gmail.com","yahoo.com","outlook.com","example.com"]
        if value.split('@')[-1] not in valid:
            raise ValueError("Invalid email domain")
        return value
#ek se jayda field se kuch validate toh isse use kar 
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age>60 and 'emergency_contact' not in self.contacts:
            raise ValueError("Emergency contact is required for patients above 60 years old")
        return self
    
    #yaha pe ek filed baayi jo height and weight se calclate hoti and ye int aur sun isse aceess vaise hi .bmi se kar sakta 
    @computed_field
    @property
    def bmi(self)->int:
        return self.weight/(self.height**2)

def patentdata(patient:User):
    print(patient.name)
    print(patient.weight)
    print(patient.height)
    print(patient.feedback)
    print(patient.metadata)
    print(patient.email)
    print(patient.website)
    print(patient.bmi)

patient={
    "name":"John Doe",
    "weight":70.5,
     "age":65,
     "contacts":{"emergency_contact":1234567890},

   
    "metadata":{"id": "12345", "created_at": "2023-01-01"},
    "email":"abc@example.com",
    "website":"https://www.example.com"

}

patient_para=User(**patient)
patentdata(patient_para)



