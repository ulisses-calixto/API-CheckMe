from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def user_check():
    return {"status": "Rodando"}