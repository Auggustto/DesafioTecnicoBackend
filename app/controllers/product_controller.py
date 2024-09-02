
from fastapi import HTTPException

from app.models.product_models import ProductModels
from app.services.product_service import ProductService


class ProductController:
    def __init__(self):
        self.product_service = ProductService()
        
    def create_product(self, name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues):
        try:            
            return self.product_service.create_product(name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
    def read_product(self, id_product):
        try:
            return self.product_service.read_product(id_product)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    
    def update_product(self, id_product, name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues):
        try:
            client = ProductModels()
            return client.update(id_product, name, susep, expirationDate, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    
    def delete_product(self, id_product):
        try:
            return self.product_service.delete_product(id_product)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))