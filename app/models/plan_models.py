import logging
from fastapi import HTTPException
from datetime import datetime

# from app.models.database.database_models import db, Plan
from app.models.database.connect_database import db
from app.models.database.new_database_models import  Plan
from app.validators.global_validation import generator_id


class PlanModels:
    
    def filter_all_plan(self, planId):
        try:
            return db.query(Plan).filter_by(id_plan=planId).all()
        except Exception as e:
            logging.error({"filter_plan_error": e})
            raise e
    
    def filter_plan(self, planId):
        try:
            return db.query(Plan).filter_by(id_plan=planId).first()
        except Exception as e:
            logging.error({"filter_plan_error": e})
            raise e

    def create(self, clientId, productId, contribution, retirementAge, statusPlan = True):
        try:
            id_plan = generator_id()
            new_plan = Plan(
                clientId=clientId,
                productId=productId,
                contribution=contribution,
                contractingDate=datetime.strptime(
                    datetime.now().strftime("%Y-%m-%d"), '%Y-%m-%d').date(),
                retirementAge=retirementAge,
                statusPlan = statusPlan,
                id_plan=id_plan
            )
            db.add(new_plan)
            db.commit()

            return {"id": id_plan}

        except HTTPException as e:
            logging.error({"create_product_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"create_product_error": e})
            raise
    
    
    def read(self, planId):
        try:
            check_plan = self.filter_plan(planId)
            if check_plan:
                return {
                    "id" : check_plan.id,
                    "clientId" : check_plan.clientId,
                    "productId" : check_plan.productId, 
                    "contribution" : check_plan.contribution, 
                    "contractingDate" : check_plan.contractingDate, 
                    "retirementAge" : check_plan.retirementAge, 
                    "statusPlan" : check_plan.statusPlan,
                    "id_plan" : check_plan.id_plan, 
                }
            
            raise HTTPException(status_code=400, detail=f"ID {planId} not found.")
            
        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e
        
        except Exception as e:
            logging.error({"read_client_error": e})
            raise
    
    
    def update(self, planId):
        try:
            check_plan = self.filter_plan(planId)
            if check_plan:
                check_plan.statusPlan = False
                db.commit()

                return {"message": "Status updated successfully!"}
            raise HTTPException(
                status_code=400, detail=f"Plan ID {planId} not found.")

        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"read_client_error": e})
            raise