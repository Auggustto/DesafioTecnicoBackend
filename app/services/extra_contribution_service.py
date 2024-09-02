# Para realizar um aporte extra, é necessário que o cliente atenda as regras definidas no produto.

from fastapi import HTTPException

from app.models.extra_contribution_models import ExtraContributionModels
from app.models.plan_models import PlanModels
from app.models.client_models import ClientModels
from app.validators.extra_contribution_validation import validate_extra_contribution


class ExtraContributionService:

    def validations_extra_contribution(sef, ClientId, contributionValue, planId):

        client = ClientModels()
        check_client = client.filter_id_client(ClientId)
        
        if not check_client:
            raise HTTPException(
                status_code=400, detail=f"Client id {ClientId} not found.")
        
        
        filter_plan = PlanModels()
        metadata_plan= filter_plan.filter_plan(planId)
        
        if not metadata_plan:
            raise HTTPException(
                status_code=400, detail=f"Plan id {planId} not found.")
        
        min_value_extra_contribution = metadata_plan.product.minValueExtraContribution
        
        validate_extra_contribution(contributionValue, min_value_extra_contribution)


    def create_extra_contribution(self, ClientId, planId, contributionValue):
        if not all([ClientId, planId, contributionValue]):
            raise HTTPException(
                status_code=400, detail="ClientId, planId and contributionValue are required")

        self.validations_extra_contribution(ClientId, contributionValue, planId)

        extra_contribution = ExtraContributionModels()
        return extra_contribution.create(ClientId, planId, contributionValue)
    
    
    def read_extra_contribution(self, id_ExtraContribution):
        if not id_ExtraContribution:
            raise HTTPException(
                status_code=400, detail="Extra Contribution ID are required.")

        extra_contribution = ExtraContributionModels()
        return extra_contribution.read(id_ExtraContribution)
