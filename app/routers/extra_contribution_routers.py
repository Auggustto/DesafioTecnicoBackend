from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.extra_contribution_controller import ExtraContributionController

router_extra_ontribution = APIRouter()


class MetadataExtraContribution(BaseModel):
    ClientId: str
    planId: str
    contributionValue: float


@router_extra_ontribution.post("/api/devel/desafioTecnicoBackend/plan/extra_contribution", tags=["Aporte Extra"])
def create(metada: MetadataExtraContribution):
    extra_contribution = ExtraContributionController()
    return extra_contribution.create_extra_contribution(metada.ClientId, metada.planId, metada.contributionValue)


@router_extra_ontribution.get("/api/devel/desafioTecnicoBackend/plan/extra_contribution/{id_ExtraContribution}", tags=["Aporte Extra"])
def create(id_ExtraContribution: str):
    extra_contribution = ExtraContributionController()
    return extra_contribution.read_extra_contribution(id_ExtraContribution)
