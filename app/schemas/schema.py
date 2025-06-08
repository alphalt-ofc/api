from pydantic import BaseModel

class MensagemBase(BaseModel):
    conteudo: str

class MensagemCreate(MensagemBase):
    pass

class Mensagem(MensagemBase):
    id: int

    class Config:
        from_attributes = True

class MensagemOut(BaseModel):
    id: int
    conteudo: str

    class Config:
        from_attributes = True