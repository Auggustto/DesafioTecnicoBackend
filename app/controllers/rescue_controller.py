
from fastapi import HTTPException
from app.services.rescue_service import RescueService


class RescueController:

    def create_rescue(self, planId, clientId, rescueValue):
        try:
            rescue = RescueService()
            return rescue.create_rescue(planId, clientId, rescueValue)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    
    def read_rescue(self, planId):
        try:
            rescue = RescueService()
            return rescue.read_rescue(planId)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
