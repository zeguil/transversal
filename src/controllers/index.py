
from schemas.data import *
from sqlalchemy import desc
from decouple import config
from fastapi import HTTPException
from config.database import Session
from models.data import DadosClimaticos

class DadosClimaticosController():
    def __init__(self, db: Session):
        self.db = db

    def read_dados(self, cidade):
        try:
            dados = self.db.query(DadosClimaticos).filter_by(cidade=cidade).order_by(desc(DadosClimaticos.id)).first()

            dados.temperatura = int(dados.temperatura)
            dados.sensacao_termica = int(dados.sensacao_termica)
            if dados.cidade == "Sao Paulo":
                dados.cidade = "São Paulo"
                dados.estado = "São Paulo"

            return dados
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=f"Erro ao buscar dados climáticos: {str(e)}")
        
    

