from datetime import datetime
from fastapi import HTTPException


def validate_contracting_plan(check_product, check_client, contribution, retirementAge):
    print(check_product, check_client, contribution, retirementAge)

    if not check_product:
        raise HTTPException(status_code=400, detail=f"Product ID not found.")

    if not check_client:
        raise HTTPException(status_code=400, detail=f"Client ID not found.")

    if contribution < 1000:
        raise HTTPException(
            status_code=400, detail="Minimum contribution allowed is R$ 1,000.00.")

    if (datetime.now() - datetime.strptime(str(check_client.birthdate), "%Y-%m-%d")).days // 365 < 18:
        raise HTTPException(
            status_code=400, detail="The minimum age to buy the product is 18 years.")

    if (datetime.strptime(str(check_product.expirationDate), "%Y-%m-%d")) < (datetime.strptime(str(datetime.now().strftime("%Y-%m-%d")), "%Y-%m-%d")):
        raise HTTPException(status_code=400, detail="The product has expired.")

    if retirementAge < check_product.exitAge:
        raise HTTPException(
            status_code=400, detail="The maximum age to start receiving the benefit is 60.")
