import uvicorn
from time import sleep
from config.database import Base, engine
from models.data import Usuario, DadosClimaticos
from routers.index import router
from routers.bot import poster
from routers.usuario import user

from sqlalchemy import inspect
from schemas.data import UserRequest
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



inspector = inspect(engine)

# Verificar se as tabelas já existem no banco de dados
existing_tables = inspector.get_table_names()
if not existing_tables:
    # Cria as tabelas apenas se elas ainda não existirem
    Base.metadata.create_all(bind=engine)
# else:
#     Base.metadata.drop_all(bind=engine)
#     print("todas as tabelas foram deletadas")


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
]

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(user)
app.include_router(poster)

@app.get("/")
def read_root(request: Request):
    data = {
        "cidade" : "Rio de Janeiro, RJ",
        "temperatura": 32,
        "sensacao_termica": 35,
        "descricao_tempo": "Ensolarado",
        "iqa": 25,
        "status": "Bom"
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="localhost")
