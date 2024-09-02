
from fastapi import HTTPException
from app.services.extra_contribution_service import ExtraContributionService


class ExtraContributionController:

    def create_extra_contribution(self, ClientId, planId, contributionValue):
        try:
            plan = ExtraContributionService()
            return plan.create_extra_contribution(ClientId, planId, contributionValue)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    
    def read_extra_contribution(self, id_ExtraContribution):
        try:
            plan = ExtraContributionService()
            return plan.read_extra_contribution(id_ExtraContribution)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
