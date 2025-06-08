from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schema import Mensagem, MensagemCreate, MensagemOut 
from app.controllers import controller
from app.database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#response_model recebe o formato da resposta do schema.py]

#@router.post("/mensagens", response_model=Mensagem)
#@router.get("/mensagens", response_model=list[Mensagem])
#@router.get("/mensagens/{mensagem_id}", response_model=Mensagem)
#@router.put("/mensagens/{mensagem_id}", response_model=Mensagem)
#@router.delete("/mensagens/{mensagem_id}")

@router.post("/mensagens", response_model=Mensagem)
def create_mensagem(mensagem: MensagemCreate, db: Session = Depends(get_db)):
    return controller.create_mensagem(db, mensagem)

@router.get("/mensagens", response_model=list[Mensagem])
def read_mensagens(db: Session = Depends(get_db)):
    return controller.get_mensagens(db)

@router.get("/mensagens/{mensagem_id}", response_model=Mensagem)
def read_mensagem(mensagem_id: int, db: Session = Depends(get_db)):
    controller.http_404_error(db, mensagem_id)
    return controller.get_mensagem(db, mensagem_id)

@router.put("/mensagens/{mensagem_id}", response_model=Mensagem)
def update_mensagem(mensagem_id: int, mensagem: MensagemCreate, db: Session = Depends(get_db)):
    controller.http_404_error(db, mensagem_id)
    return controller.update_mensagem(db, mensagem_id, mensagem.conteudo)

@router.delete("/mensagens/{mensagem_id}")
def delete_mensagem(mensagem_id: int, db: Session = Depends(get_db)):
    mensagem = controller.http_404_error(db, mensagem_id)   
    controller.delete_mensagem(db, mensagem_id)                                  
    return {
    "mensagem": MensagemOut.model_validate(mensagem),
    "status": "message deleted successfully"
    }