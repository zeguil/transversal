
from schemas.data import *
from decouple import config
from models.data import DadosClimaticos
from fastapi import HTTPException
from config.database import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc


class DataController():
    def __init__(self, db: Session):
        self.db = db


    def create_data(self, dados: DadosClimaticosCreate):
        try:
            novo_dado = DadosClimaticos(
                cidade=dados.cidade,
                estado = dados.estado,
                iqa=dados.iqa,
                poluente=dados.poluente,
                status=dados.status,
                poluente_sig=dados.poluente_sig,
                descricao_tempo=dados.descricao_tempo,
                temperatura=dados.temperatura,
                sensacao_termica=dados.sensacao_termica,
                umidade=dados.umidade,
                velocidade_vento=dados.velocidade_vento
            )
            self.db.add(novo_dado)
            self.db.commit()
            self.db.refresh(novo_dado)
            return novo_dado
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar dados climáticos: {str(e)}")

    def update_data(self, dados_update: DadosClimaticosCreate):
        try:
            data = self.db.query(DadosClimaticos).filter(DadosClimaticos.email == dados_update.email).first()
            if not data:
                raise HTTPException(status_code=404, detail="Dados não encontrados")

            if dados_update.cidade:
                data.cidade = dados_update.cidade
            if dados_update.iqa:
                data.iqa = dados_update.iqa
            if dados_update.poluente:
                data.poluente = dados_update.poluente
            if dados_update.status:
                data.status = dados_update.status
            if dados_update.poluente_sig:
                data.poluente_sig = dados_update.poluente_sig
            if dados_update.descricao_tempo:
                data.descricao_tempo = dados_update.descricao_tempo
            if dados_update.temperatura:
                data.temperatura = dados_update.temperatura
            if dados_update.sensacao_termica:
                data.sensacao_termica = dados_update.sensacao_termica
            if dados_update.umidade:
                data.umidade = dados_update.umidade
            if dados_update.velocidade_vento:
                data.velocidade_vento = dados_update.velocidade_vento

            self.db.commit()
            self.db.refresh(data)

            return data
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500, detail=f"Internal Server Error: {str(e)}")
        
    def delete_dados(self):
        try:
            # Busca os sete registros mais antigos e os exclui para não pesar o banco
            dados_a_excluir = self.db.query(DadosClimaticos).order_by(desc(DadosClimaticos.id)).limit(14).all()
            for dado in dados_a_excluir:
                self.db.delete(dado)
            self.db.commit()
            return {"message": "Os sete registros mais antigos foram excluídos com sucesso."}
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=f"Erro ao excluir registros antigos: {str(e)}")


