from pydantic import BaseModel

#nested model

class Address(BaseModel):
    street:str
    city:str
    state:str
    zip_code:str


class User(BaseModel):
    name:str
    age:int
    address:Address


add={"street":"123 Main St",
     "city":"New York",
     "state":"NY",
     "zip_code":"10001"}

address=Address(**add)

user={"name":"John Doe",
      "age":30,
      "address":address}

user1=User(**user)

print(user1.model_dump()) #isse dict m change
print(user1.model_dump_json()) #isse json m change
print(user1.model_dump(include={"name","age"})) #isse sirf name aur age aayega dict m
print(user1.model_dump_json(exclude={"address":["street"]})) #isse address ka street exclude hoga sirf
