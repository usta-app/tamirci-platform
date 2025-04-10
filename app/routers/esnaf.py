from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Esnaf
from app.schemas import EsnafKayit
from app.utils import hash_password

router = APIRouter()

@router.post("/register")
def esnaf_kayit(esnaf: EsnafKayit, db: Session = Depends(get_db)):
    mevcut = db.query(Esnaf).filter(Esnaf.telefon == esnaf.telefon).first()
    if mevcut:
        raise HTTPException(status_code=400, detail="Bu telefon numarası zaten kayıtlı.")
    
    yeni_esnaf = Esnaf(
        dukkan_adi=esnaf.isim,  # Burada isim yerine dükkan adı alınıyor
        telefon=esnaf.telefon,
        email=esnaf.email,
        sifre=hash_password(esnaf.sifre),
        hizmet_alani=esnaf.hizmet_alani if esnaf.hizmet_alani else "Belirtilmemiş"  # eksik alanı kontrol et
    )
    
    db.add(yeni_esnaf)
    db.commit()
    db.refresh(yeni_esnaf)
    
    return {"mesaj": "Esnaf başarıyla kaydedildi", "esnaf_id": yeni_esnaf.id}
