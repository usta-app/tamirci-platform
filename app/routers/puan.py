from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def puan_test():
    return {"mesaj": "Puan modülü çalışıyor!"}
