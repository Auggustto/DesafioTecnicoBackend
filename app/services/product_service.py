
from fastapi import HTTPException

from app.models.product_models import ProductModels
from app.validators.global_validation import convert_date
from app.validators.global_validation import check_date


class ProductService:

    def create_product(self, name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues):
        if not all([name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues]):
            raise HTTPException(status_code=400, detail="cpf, name, email, birthdate, gender, monthlyIncome are required.")
        
        date = convert_date(expirationDate)
        check_date(date)
        
        product = ProductModels()
        return product.create(name, susep, date, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues)
    
    
    def read_product(self, id_product):
        if not id_product:
            raise HTTPException(status_code=400, detail="ID are required!")
        
        product = ProductModels()
        return product.read(id_product)
    
    
    def update_product(self, id_product, name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues):
        if not all([id_product, name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues]):
            raise HTTPException(status_code=400, detail="cpf, name, email, birthdate, gender, monthlyIncome are required!")

        date = convert_date(expirationDate)
        check_date(date)

        client = ProductModels()
        return client.update(id_product, name, susep, date, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues)
    
    
    def delete_product(self, id_product):
        if not id_product:
            raise HTTPException(status_code=400, detail="ID are required!")
    
        product = ProductModels()
        return product.delete(id_product)