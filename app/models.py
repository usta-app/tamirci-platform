from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.database import Base
import datetime

class Kullanici(Base):
    __tablename__ = "kullanicilar"
    id = Column(Integer, primary_key=True)
    isim = Column(String)
    telefon = Column(String, unique=True)
    email = Column(String)
    sifre = Column(String)
    arac_turu = Column(String)
    puan = Column(Integer, default=0)
    kayit_tarihi = Column(DateTime, default=datetime.datetime.utcnow)

class Esnaf(Base):
    __tablename__ = "esnaflar"
    id = Column(Integer, primary_key=True)
    dukkan_adi = Column(String)
    adres = Column(String)
    telefon = Column(String, unique=True)
    sifre = Column(String)
    hizmet_alani = Column(String)
    puan = Column(Float, default=0.0)
    kayit_tarihi = Column(DateTime, default=datetime.datetime.utcnow)
