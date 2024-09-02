from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.plan_controller import PlanController

router_plan = APIRouter()


class MetadataPlan(BaseModel):
    clientId: str
    productId: str
    contribution: float
    retirementAge: int


@router_plan.post("/api/devel/desafioTecnicoBackend/plan", tags=["Contratação de plano"])
def create(metada: MetadataPlan):
    plan = PlanController()
    return plan.create_plan(metada.clientId, metada.productId, metada.contribution, metada.retirementAge)


@router_plan.get("/api/devel/desafioTecnicoBackend/plan/{planId}", tags=["Contratação de plano"])
def read(planId: str):
    plan = PlanController()
    return plan.read_plan(planId)


