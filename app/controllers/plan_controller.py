
from fastapi import HTTPException
from app.services.plan_service import PlanService


class PlanController:

    def create_plan(self, clientId, productId, contribution, retirementAge):
        try:
            plan = PlanService()
            return plan.contracting_plan(clientId, productId, contribution, retirementAge)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def read_plan(self, planId):
        try:
            plan = PlanService()
            return plan.read_plan(planId)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def update_plan(self, planId):
        try:
            plan = PlanService()
            return plan.update_plan(planId)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
