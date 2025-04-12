from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.routers import kullanici, esnaf
from app.models import Esnaf
from app.schemas import EsnafKayit  # EsnafKayit Pydantic modelini import et

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Kullanıcı ve Esnaf router'larını ekliyoruz
app.include_router(kullanici.router, prefix="/api/kullanici", tags=["Kullanıcı"])
app.include_router(esnaf.router, prefix="/api/esnaf", tags=["Esnaf"])

@app.get("/test")
def test_endpoint():
    return {"message": "API çalışıyor!"}

@app.post("/api/esnaf")
def create_esnaf(esnaf: EsnafKayit, db: Session = Depends(get_db)):
    db_esnaf = Esnaf(**esnaf.dict())  # Pydantic modelinden veriyi Esnaf modeline çevir
    db.add(db_esnaf)
    db.commit()
    db.refresh(db_esnaf)
    return db_esnaf






