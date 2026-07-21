from fastapi import FastAPI,Request
from models import User,user_response,Base
from database import engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"), name ="static")
@app.get("/")
def homepage(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
@app.post("/signup", response_model=user_response)
def signup(user:User):
    return{
        "id":1,
        "name":user.name,
        "age":user.age,
        "password":"12356"
    }
@app.get("/submit")
def submit():
    print("button clicked!")
    return{
        "message":"user data submitted successfully"
    }