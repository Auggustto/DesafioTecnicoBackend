# Para realizar o resgate, é necessário que o cliente atenda as regras de resgate definidas no produto.
# Um plano sem saldo estará automacamente cancelado, não podendo mais haver nenhuma operação no mesmo

from fastapi import HTTPException

from app.models.rescue_models import RescueModels
from app.models.plan_models import PlanModels
from app.models.extra_contribution_models import ExtraContributionModels
from app.validators.rescue_validation import validate_rescue


class RescueService:

    def create_rescue(self, planId, clientId, rescueValue):
        
        if not all([planId, rescueValue]):
            raise HTTPException(
                status_code=400, detail="Plan Id and rescue value is required")
            
        validate_rescue(planId, clientId, rescueValue)
        
        rescue = RescueModels()
        return rescue.create(planId, clientId, rescueValue)
    
    
    def read_rescue(self, planId):
        if not planId:
            raise HTTPException(status_code=400, detail="ID are required!")
        
        rescue = RescueModels()
        return rescue.read(planId)
