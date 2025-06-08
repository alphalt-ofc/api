from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes import routes

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routes.router)