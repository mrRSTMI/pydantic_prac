from fastapi import HTTPException
from database.data import products


def order_calc(items):
    total = 0
    selected_products = []

    for item in items:
        product = next(
            (p for p in products if p["id"] == item.product_id),
            None
        )

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if item.quantity > product["quantity"]:
            raise HTTPException(
                status_code=400,
                detail="Not enough stock"
            )

        total += product["price"] * item.quantity

        selected_products.append((product, item.quantity))

    for product, quantity in selected_products:
        product["quantity"] -= quantity

    return total