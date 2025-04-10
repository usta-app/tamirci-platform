from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def randevu_test():
    return {"mesaj": "Randevu modülü çalışıyor!"}
