from datetime import datetime
from fastapi import HTTPException
from app.models.plan_models import PlanModels


from app.models.rescue_models import RescueModels
from app.models.plan_models import PlanModels
from app.models.extra_contribution_models import ExtraContributionModels

def filter_values(planId, clientId):
    
    # checking redemption criteria 
    rescue = PlanModels()
    check_plan = rescue.filter_plan(planId)
            
    # checking all extra contribution
    extra_contribuition = ExtraContributionModels()
    check_extra_contribuition = extra_contribuition.filter_all_extra_contribution(check_plan.clientId)
    
    # Filter rescue values
    filter_rescues = RescueModels()
    filter_rescue = filter_rescues.filter_all_rescue(clientId)
    
    return check_plan, check_extra_contribuition, filter_rescue



def validate_rescue(planId, clientId, rescueValue ):
    
    check_plan, check_extra_contribuition, filter_rescue = filter_values(planId, clientId)
    

    if not check_plan:
        raise HTTPException(status_code=400, detail=f"Plan ID {check_plan} not found.")
    
    if check_plan.statusPlan == False:
        print("deu boa")
    
    if (datetime.now() - datetime.strptime(str(check_plan.client.birthdate), "%Y-%m-%d")).days // 365 < check_plan.product.minValueExtraContribution:
        raise HTTPException(
            status_code=400, detail="The minimum age to start receiving the benefit is 60.")

    # validation balance
    contribution = check_plan.contribution
    value_extra_contribution = sum([contribuitions.contributionValue for contribuitions in check_extra_contribuition]) + contribution
    value_resuce = sum([rescue.rescueValue for rescue in filter_rescue])

    if  rescueValue > (value_extra_contribution - value_resuce):
        
        # if the account value is 0 change the status 
        satatus_plan = PlanModels()
        satatus_plan.update(planId)
        
        raise HTTPException(
            status_code=400, detail=f"Please note that the redemption value is higher than the balance: {value_extra_contribution - value_resuce}.")
    
    return value_extra_contribution - value_resuce