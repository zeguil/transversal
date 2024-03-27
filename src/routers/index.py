# routers.py
from fastapi import APIRouter
from config.database import Session
from fastapi.requests import Request
from fastapi import APIRouter, Depends
from config.dependencies import get_db
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from controllers.index import DadosClimaticosController

router = APIRouter()

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/mao")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Manaus")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/cr")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Curitiba")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/st")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Santarem")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/pm")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Palmas")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/pv")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Porto Velho")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/rb")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Rio Branco")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/sp")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Sao Paulo")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@router.get("/rf")
def read_root(request: Request, db: Session = Depends(get_db)):
    data = DadosClimaticosController(db).read_dados("Recife")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})



