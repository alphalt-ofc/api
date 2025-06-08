from sqlalchemy.orm import Session
from app.models.model import Mensagem
from app.schemas.schema import MensagemCreate
from fastapi import HTTPException

def http_404_error(db: Session, mensagem_id: int):
    mensagem = get_mensagem(db, mensagem_id)
    if not mensagem:
        raise HTTPException(status_code=404, detail="Message not found")
    return mensagem

def get_mensagens(db: Session):
    return db.query(Mensagem).all()

def get_mensagem(db: Session, mensagem_id: int):
    mensagem = db.query(Mensagem).filter(Mensagem.id == mensagem_id).first()
    if not mensagem:
        return False
    return mensagem

def create_mensagem(db: Session, mensagem: MensagemCreate):
    db_mensagem = Mensagem(conteudo=mensagem.conteudo)
    db.add(db_mensagem)
    db.commit()
    db.refresh(db_mensagem)
    return db_mensagem

def update_mensagem(db: Session, mensagem_id: int, conteudo: str):
    db_mensagem = get_mensagem(db, mensagem_id)
    db_mensagem.conteudo = conteudo
    db.commit()
    db.refresh(db_mensagem)
    return db_mensagem

def delete_mensagem(db: Session, mensagem_id: int):
    db_mensagem = get_mensagem(db, mensagem_id)
    if db_mensagem:
        db.delete(db_mensagem)
        db.commit()
    return db_mensagem