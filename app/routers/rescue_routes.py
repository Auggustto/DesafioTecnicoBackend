from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.rescue_controller import RescueController

router_rescue = APIRouter()


class MetadataRescue(BaseModel):
    planId: str
    clientId : str
    rescueValue: float


@router_rescue.post("/api/devel/desafioTecnicoBackend/plan/rescue", tags=["Resgate"])
def create(metada: MetadataRescue):
    rescue = RescueController()
    return rescue.create_rescue(metada.planId, metada.clientId, metada.rescueValue)


@router_rescue.get("/api/devel/desafioTecnicoBackend/plan/rescue/{planId}", tags=["Resgate"])
def create(planId: str):
    rescue = RescueController()
    return rescue.read_rescue(planId)
