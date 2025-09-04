from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def me():
    return {
        "nome": "Ulisses Calixto",
        "email": "ulisses@email.com",
        "curso": "Sistemas de Informação",
        "GitHub": "ulisses-calixto",
        "Cidade": "Crato-Ce",
        "Interesses": "Tecnologia, design, UX-UI, inovação, música, etc."
    }