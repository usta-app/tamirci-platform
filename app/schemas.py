from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Kullanıcı Kayıt Şeması
class KullaniciKayit(BaseModel):
    isim: str
    telefon: str
    email: str
    sifre: str
    arac_turu: str

# Kullanıcı Cevap Şeması
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

# Esnaf Kayıt Şeması
class EsnafKayit(BaseModel):
    dukkan_adi: str
    adres: str
    telefon: str
    sifre: str
    hizmet_alani: Optional[str] = None  # hizmet alanı opsiyonel
    puan: float = 0.0

    class Config:
        orm_mode = True

# Esnaf Cevap Şeması (Bu şema esnaf bilgilerini döndürmek için kullanılacak)
class EsnafCevap(BaseModel):
    id: int
    dukkan_adi: str
    adres: str
    telefon: str
    hizmet_alani: Optional[str] = None
    puan: float
    kayit_tarihi: datetime

    class Config:
        orm_mode = True
