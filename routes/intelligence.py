from fastapi import APIRouter

router = APIRouter()

@router.get("/deals")
def get_deals():
    return {"message": "Deals endpoint working"}
