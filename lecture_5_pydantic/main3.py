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

print(user1.age)
