from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Kullanici
from app.schemas import KullaniciKayit, KullaniciCevap
from app.utils import hash_password

router = APIRouter()

@router.post("/register", response_model=KullaniciCevap)
def kullanici_kayit(kullanici: KullaniciKayit, db: Session = Depends(get_db)):
    mevcut = db.query(Kullanici).filter(Kullanici.telefon == kullanici.telefon).first()
    if mevcut:
        raise HTTPException(status_code=400, detail="Bu telefon numarası zaten kayıtlı.")
    
    yeni_kullanici = Kullanici(
        isim=kullanici.isim,
        telefon=kullanici.telefon,
        email=kullanici.email,
        sifre=hash_password(kullanici.sifre),
        arac_turu=kullanici.arac_turu
    )
    db.add(yeni_kullanici)
    db.commit()
    db.refresh(yeni_kullanici)
    return yeni_kullanici
