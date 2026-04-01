from fastapi import APIRouter

router = APIRouter(prefix="/products")

@router.get("/products")
def get_products():
    return {"msg": "All products"}
