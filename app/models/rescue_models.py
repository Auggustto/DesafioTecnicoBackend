import logging
from fastapi import HTTPException

# from app.models.database.database_models import db, Rescue
from app.models.database.connect_database import db
from app.models.database.new_database_models import  Rescue

from app.validators.global_validation import generator_id

class RescueModels:
    
    def filter_all_rescue(self, clientId):
        try:
            return db.query(Rescue).filter_by(clientId=clientId).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

    def filter_rescue(self, planId):
        try:
            return db.query(Rescue).filter_by(id_rescue=planId).first()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
    def create(self, planId, clientId, rescueValue):
        try:
            id_rescue = generator_id()
            
            check_rescue = self.filter_rescue(planId)
            print(check_rescue)
            
            if not check_rescue:
                new_rescue = Rescue(
                    planId=planId,
                    clientId=clientId,
                    rescueValue=rescueValue,
                    id_rescue=id_rescue,
                )
                db.add(new_rescue)
                db.commit()

                return {"id": id_rescue}

            raise HTTPException(status_code=400, detail=f"ID {planId} is not found")
        
        except HTTPException as e:
            logging.error({"create_product_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"create_product_error": e})
            raise
    
    
    def read(self, planId):
        try:
            check_rescue = self.filter_rescue(planId)
            if not check_rescue:
                raise HTTPException(status_code=400, detail=f"ID {planId} is not found")

            return {
                "id" : check_rescue.id,
                "planId" : check_rescue.planId,
                "rescueValue" : check_rescue.rescueValue,
                "id_rescue" : check_rescue.id_rescue,
            }
        except HTTPException as e:
            logging.error({"read_rescue_error": e.detail})
            raise e