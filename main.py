from fastapi import FastAPI,Request
from models import User,user_response,Base,UserTable
from database import engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import SessionLocal
Base.metadata.create_all(bind=engine)
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"), name ="static")
@app.get("/")
def signuppage(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
@app.post("/signup", response_model=user_response)
def signup(user:User):
    db=SessionLocal()
    db_user=UserTable(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user
@app.get("/submit")
def submit():
    print("button clicked!")
    return{
        "message":"user data submitted successfully"
    }
@app.get("/home")
def homepage(my_request:Request):
    return templates.TemplateResponse(
        request=my_request,
        name="homepage.html"
    )
@app.get("/adoptacat")
def adoptacat(my_request:Request):
    return templates.TemplateResponse(
        request=my_request,
        name="adoptacat.html"
    )
@app.get("/catstagram")
def catstagram(my_request:Request):
    return templates.TemplateResponse(
        request=my_request,
        name="catstagram.html"
    )
@app.get("/postpetforadoption")
def postpetforadoption(my_request:Request):
    return templates.TemplateResponse(
            request=my_request,
            name="postcatforadoption.html"
        )
