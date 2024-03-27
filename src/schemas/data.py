from typing import Optional
from pydantic import BaseModel


class UserRequest(BaseModel):
    nome: str
    cidade: str
    email: str

class UserResponse(BaseModel):
    nome: str
    cidade: str
    email: str

class DadosClimaticosCreate(BaseModel):
    cidade: Optional[str]
    estado: Optional[str]
    iqa: Optional[int] = None
    poluente: Optional[str] = None
    status: Optional[str] = None
    poluente_sig: Optional[str] = None
    descricao_tempo: Optional[str] = None
    temperatura: Optional[float] = None
    sensacao_termica: Optional[float] = None
    umidade: Optional[int] = None
    velocidade_vento: Optional[str] = None


class DadosClimaticosRead(BaseModel):
    cidade: str
    estado: str
    iqa: int
    poluente: str
    status: str
    poluente_sig: str
    descricao_tempo: str
    temperatura: float
    sensacao_termica: float
    umidade: int
    velocidade_vento: str

class DadosClimaticosUpdate(BaseModel):
    cidade: str
    estado: str
    iqa: int
    poluente: str
    status: str
    poluente_sig: str
    descricao_tempo: str
    temperatura: float
    sensacao_termica: float
    umidade: int
    velocidade_vento: str