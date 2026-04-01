from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import Product

router = APIRouter(prefix="/products", tags=["Products"])

# Temporary database
products = []

# CREATE
@router.post("/")
def create_product(product: Product):
    # Check duplicate ID
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product already exists")

    products.append(product)
    return {"message": "Product created", "data": product}


# READ ALL
@router.get("/")
def get_products():
    return {"products": products}


# READ ONE
@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


# UPDATE
@router.put("/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {"message": "Product updated", "data": updated_product}

    raise HTTPException(status_code=404, detail="Product not found")


# DELETE
@router.delete("/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted = products.pop(index)
            return {"message": "Product deleted", "data": deleted}

    raise HTTPException(status_code=404, detail="Product not found")