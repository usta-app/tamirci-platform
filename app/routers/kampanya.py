from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def kampanya_test():
    return {"mesaj": "Kampanya modülü çalışıyor!"}
