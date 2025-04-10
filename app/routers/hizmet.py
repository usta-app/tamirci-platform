from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def hizmet_test():
    return {"mesaj": "Hizmet modülü çalışıyor!"}
