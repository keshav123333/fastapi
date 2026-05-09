# install this pip install fastapi uvicorn pydantic
# then run this command uvicorn main:app --reload
#if tu apne url ke aage se sab hata ke docs likhoge to tumhe documentation milega
# https://potential-space-halibut-wr7xrpvq75vxc5wj9-8000.app.github.dev/docs ye codepace ka hai but apne wale m bhi

from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is a simple FastAPI application."}
# codepsce mein iss url pe hai https://potential-space-halibut-wr7xrpvq75vxc5wj9-8000.app.github.dev/about bas jo url /about likh de 