import logging
from fastapi import HTTPException

from app.models.database.connect_database import db
from app.models.database.new_database_models import  ExtraContribution
from app.validators.global_validation import generator_id


class ExtraContributionModels:
    
    def filter_all_extra_contribution(self, id_ExtraContribution):
        try:
            return db.query(ExtraContribution).filter_by(clientId=id_ExtraContribution).all()
        except Exception as e:
            logging.error({"check_client_error": e})
            raise HTTPException(
                status_code=500, ddetail="Internal Server Error")
    
    
    def filter_extra_contribution(self, id_ExtraContribution):
        try:
            return db.query(ExtraContribution).filter_by(id_ExtraContribution=id_ExtraContribution).first()
        except Exception as e:
            logging.error({"check_client_error": e})
            raise HTTPException(
                status_code=500, ddetail="Internal Server Error")
            

    def create(self, ClientId, planId, contributionValue):
        try:
            id_extra_contribution = generator_id()
            
            new_extra_contribution = ExtraContribution(
                clientId=ClientId,
                planId=planId,
                contributionValue=contributionValue,
                id_ExtraContribution=id_extra_contribution,
            )
            db.add(new_extra_contribution)
            db.commit()

            return {"id": id_extra_contribution}

        except HTTPException as e:
            logging.error({"create_product_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"create_product_error": e})
            raise
    
    
    def read(self, id_ExtraContribution):
        try:
            check_extra_contribution = self.filter_extra_contribution(id_ExtraContribution)
            if check_extra_contribution:
                return {
                    "id" : check_extra_contribution.id,
                    "ClientId" : check_extra_contribution.ClientId,
                    "planId" : check_extra_contribution.planId, 
                    "contributionValue" : check_extra_contribution.contributionValue, 
                    "id_ExtraContribution" : check_extra_contribution.id_ExtraContribution, 
                }
            
            raise HTTPException(status_code=400, detail=f"ID {id_ExtraContribution} not found.")
            
        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e
        
        except Exception as e:
            logging.error({"read_client_error": e})
            raise
