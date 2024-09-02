import logging
from fastapi import HTTPException
from app.models.database.connect_database import db
from app.models.database.new_database_models import  Product
from app.validators.global_validation import generator_id


class ProductModels:
    
    def check_product(self, id_product):
        try:
            return db.query(Product).filter_by(id_product=id_product).first()
        except Exception as e:
            logging.error({"check_product_error": e})
            raise HTTPException(status_code=500, ddetail="Internal Server Error")
        
        
    def create(self, name, susep, date, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues):
        try:
            check_product = db.query(Product).filter_by(name=name).first()
            if check_product:
                raise HTTPException(status_code=400, detail=f"Product {name} is already in use!")
            
            id_product = generator_id() 
            new_client = Product(
                name=name, 
                susep=susep, 
                expirationDate=date, 
                minValueInitialContribution=minValueInitialContribution, 
                minValueExtraContribution=minValueExtraContribution, 
                entryAge=entryAge, 
                exitAge=exitAge, 
                initialRescueWaitingPeriod=initialRescueWaitingPeriod, 
                timeBetweenRescues=timeBetweenRescues, 
                id_product=id_product
                )
            db.add(new_client)
            db.commit()

            return {"id": id_product}
        
        except HTTPException as e:
            logging.error({"create_product_error": e.detail})
            raise e
        
        except Exception as e:
            logging.error({"create_product_error": e})
            raise
        
    
    def read(self, id_product):
        try:
            check_product = self.check_product(id_product)
            if check_product:
                return {
                    "id" : check_product.id,
                    "name" : check_product.name,
                    "susep" : check_product.susep, 
                    "expirationDate" : check_product.expirationDate, 
                    "minValueInitialContribution" : check_product.minValueInitialContribution, 
                    "minValueExtraContribution" : check_product.minValueExtraContribution, 
                    "entryAge" : check_product.entryAge, 
                    "exitAge" : check_product.exitAge, 
                    "initialRescueWaitingPeriod" : check_product.initialRescueWaitingPeriod, 
                    "timeBetweenRescues" : check_product.timeBetweenRescues, 
                    "id_product" : check_product.id_product
                }
            
            raise HTTPException(status_code=400, detail=f"ID {id_product} not found.")
            
        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e
        
        except Exception as e:
            logging.error({"read_client_error": e})
            raise


    def update(self, id_product, name, susep, date, minValueInitialContribution, minValueExtraContribution, entryAge, exitAge, initialRescueWaitingPeriod, timeBetweenRescues):
        try:
            check_product = self.check_product(id_product)
            if check_product:
                check_product.name = name
                check_product.susep = susep
                check_product.expirationDate = date
                check_product.minValueInitialContribution = minValueInitialContribution
                check_product.minValueExtraContribution = minValueExtraContribution
                check_product.entryAge = entryAge
                check_product.exitAge = exitAge
                check_product.initialRescueWaitingPeriod = initialRescueWaitingPeriod
                check_product.timeBetweenRescues = timeBetweenRescues
                
                db.commit()

                return {"message": "Product updated successfully!"}
            
            raise HTTPException(status_code=400, detail=f"ID {id_product} not found.")
        
        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e
        
        except Exception as e:
            logging.error({"read_client_error": e})
            raise


    def delete(self, id_product):
        try:
            check_client = self.check_product(id_product)
            if check_client:
                db.delete(check_client)
                db.commit()
                return {"message": f"ID {id_product} deleted successfully!"}
            
            raise HTTPException(status_code=400, detail=f"ID {id_product} not found.")
        
        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e
        
        except Exception as e:
            logging.error({"read_client_error": e})
            raise