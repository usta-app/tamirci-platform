from fastapi import FastAPI
from app.database import Base, engine
from app.routers import kullanici, esnaf  # Esnaf ve Kullanıcı router'larını doğru şekilde ekleyelim

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Kullanıcı ve Esnaf router'larını ekliyoruz
app.include_router(kullanici.router, prefix="/api/kullanici", tags=["Kullanıcı"])
app.include_router(esnaf.router, prefix="/api/esnaf", tags=["Esnaf"])
@app.get("/test")
def test_endpoint():
    return {"message": "API çalışıyor!"}



