from decouple import config
from sqlalchemy import desc
from fastapi import HTTPException
from config.database import Session
from schemas.data import UserRequest
from mail.sendmail import send_email
from celeryDir.tasks import send_email_async
from sqlalchemy.exc import IntegrityError
from models.data import Usuario, DadosClimaticos

class UserController():
    def __init__(self, db: Session):
        self.db = db


    def create_user(self, dados: UserRequest):
        try:
            # Verificar se o e-mail já existe
            if self.db.query(Usuario).filter(Usuario.email == dados.email).first():
                raise HTTPException(status_code=400, detail="Este e-mail já está em uso")
            novo_usuario = Usuario(
                nome=dados.nome,
                cidade=dados.cidade,
                email=dados.email
            )
            self.db.add(novo_usuario)
            self.db.commit()
            self.db.refresh(novo_usuario)

            dados = self.db.query(DadosClimaticos).filter_by(cidade=novo_usuario.cidade).order_by(desc(DadosClimaticos.id)).first()
            
            # send_email(email=novo_usuario.email, cidade=novo_usuario.cidade, nome=novo_usuario.nome, status=dados.status, iqa=dados.iqa)
            try:
                print("enviando email")
                # send_email_async.delay(email=novo_usuario.email, cidade=novo_usuario.cidade, nome=novo_usuario.nome, status=dados.status, iqa=dados.iqa)
                return novo_usuario
            except:
                print("erro ao enviar email")
        except IntegrityError as e:
            print(e)
            raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")
        
    def read_users(self):
        try:
            usuarios = self.db.query(Usuario).all()
            return usuarios
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao ler usuários: {str(e)}")
