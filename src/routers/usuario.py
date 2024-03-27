from time import sleep
from schemas.data import *
from config.database import Session
from fastapi import APIRouter, Depends
from config.dependencies import get_db
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request, Form
from controllers.usuario import UserController
from fastapi.templating import Jinja2Templates
from schemas.data import UserRequest, UserResponse

user = APIRouter()

templates = Jinja2Templates(directory="templates")
@user.get("/cadastro", response_class=HTMLResponse)
async def show_form(request: Request):
    data = {"return": None}
    return templates.TemplateResponse("form.html", {"request": request, "data": data})

@user.post("/cadastro")
async def process_form(request: Request, nome: str = Form(...), email: str = Form(...), cidade: str = Form(...), db: Session = Depends(get_db)):
    try:
        dados = UserRequest(nome=nome, email=email, cidade=cidade)
        UserController(db).create_user(dados)
        sleep(2)
        data = {"return": "EMAIL CADASTRADO COM SUCESSO!\n -verifique seu email."}
        return templates.TemplateResponse("form.html", {"request": request, "data":data})
    except Exception as e:
        print(e)
        data = {"return": "ERRO AO CADASTRAR EMAIL."}
        return templates.TemplateResponse("form.html", {"request": request, "data":data})
    

@user.get("/usuarios/", response_model=list[UserResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = UserController(db).read_users()
    return usuarios
