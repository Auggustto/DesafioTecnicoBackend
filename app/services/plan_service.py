# Para o cliente contratar um plano, é necessário que esteja dentro do período de venda e acima do aporte mínimo do produto.

from fastapi import HTTPException

from app.models.product_models import ProductModels
from app.models.client_models import ClientModels
from app.models.plan_models import PlanModels
from app.validators.plan_validation import validate_contracting_plan


class PlanService:

    def validations_contracting_plan(sef, productId, clientId, contribution, retirementAge):

        product = ProductModels()
        check_product = product.check_product(productId)

        client = ClientModels()
        check_client = client.filter_id_client(clientId)

        validate_contracting_plan(
            check_product, check_client, contribution, retirementAge)


    def contracting_plan(self, clientId, productId, contribution, retirementAge):
        if not all([clientId, productId, contribution, retirementAge]):
            raise HTTPException(status_code=400, detail="cpf, name, email, birthdate, gender, monthlyIncome are required.")

        # Validation contracting plan
        self.validations_contracting_plan(productId, clientId, contribution, retirementAge)
        
        plan = PlanModels()
        return plan.create(clientId, productId, contribution, retirementAge)
    
    
    def read_plan(self, planId):
        if not planId:
            raise HTTPException(
                status_code=400, detail="Plan id  are required.")
        
        plan = PlanModels()
        return plan.read(planId)
    
    def update_plan(self, planId):
        if not planId:
            raise HTTPException(
                status_code=400, detail="Plan id  are required.")
        
        plan = PlanModels()
        return plan.update(planId)
        
        
