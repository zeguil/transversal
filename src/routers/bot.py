from fastapi import APIRouter, HTTPException
from schemas.data import *
from config.database import Session
from fastapi import APIRouter, Depends
from config.dependencies import get_db
from controllers.poster import DataController
from models.data import DadosClimaticos
from schemas.data import DadosClimaticosCreate, DadosClimaticosRead
from sqlalchemy.exc import IntegrityError


poster = APIRouter()

@poster.post("/dados_climaticos/create", response_model=DadosClimaticosCreate)
def create_dados_climaticos(dados: DadosClimaticosCreate, db: Session = Depends(get_db)):
    try:
        data = DataController(db).create_data(dados)
        return data
    except Exception as e:
        return e

@poster.post("/dados_climaticos/update", response_model=DadosClimaticosRead)
def update_dados_climaticos(dados: DadosClimaticosCreate, db: Session = Depends(get_db)):
    try:
        # Cria uma nova instância do modelo com base nos dados recebidos
        novo_dado = DadosClimaticos(**dados.dict())
        # Adiciona e commita ao banco de dados
        db.add(novo_dado)
        db.commit()
        db.refresh(novo_dado)
        return novo_dado
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Erro ao criar dados climáticos: Registro já existe")

# Rota para obter todos os registros de dados climáticos
@poster.get("/dados_climaticos/read", response_model=list[DadosClimaticosRead])
def get_dados_climaticos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(DadosClimaticos).offset(skip).limit(limit).all()



@poster.delete("/dados_climaticos/delete/{id}", response_model=dict)
def delete_dados_climaticos(id: int, db: Session = Depends(get_db)):
    try:
        print("entrou")
        data = DataController(db).delete_dados()
        return data
    except Exception as e:
        return e


