from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class KullaniciKayit(BaseModel):
    isim: str
    telefon: str
    email: str
    sifre: str
    arac_turu: str

class KullaniciCevap(BaseModel):
    id: int
    isim: str
    telefon: str
    email: str
    arac_turu: str
    puan: int
    kayit_tarihi: datetime

    class Config:
        orm_mode = True
class EsnafKayit(BaseModel):
    isim: str
    telefon: str
    email: str
    sifre: str
    hizmet_alani: Optional[str] = None  # hizmet alanı opsiyonel
