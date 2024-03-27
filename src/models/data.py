from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, index=True)
    cidade = Column(String, index=True)


class DadosClimaticos(Base):
    __tablename__ = 'dados_climaticos'

    id = Column(Integer, primary_key=True)
    cidade = Column(String, nullable=True)
    estado = Column(String, nullable=True)
    iqa = Column(Integer, nullable=True)
    poluente = Column(String, nullable=True)
    status = Column(String, nullable=True)
    poluente_sig = Column(String, nullable=True)
    descricao_tempo = Column(String, nullable=True)
    temperatura = Column(Float, nullable=True)
    sensacao_termica = Column(Float, nullable=True)
    umidade = Column(Integer, nullable=True)
    velocidade_vento = Column(String, nullable=True)