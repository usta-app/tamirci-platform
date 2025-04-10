from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def yorum_test():
    return {"mesaj": "Yorum modülü çalışıyor!"}
