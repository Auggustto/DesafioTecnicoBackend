from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.client_controller import ClientController
from starlette.responses import RedirectResponse

router_client = APIRouter()


class MetadataClient(BaseModel):
    cpf:str
    name:str
    email:str
    birthdate:str
    gender:str
    monthlyIncome:float
    

@router_client.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

@router_client.post("/brasilprev/api/client", tags=["Cadastro de cliente"])
def create(metada : MetadataClient):
    client = ClientController()
    return client.create_client(metada.cpf, metada.name, metada.email, metada.birthdate, metada.gender, metada.monthlyIncome)

@router_client.get("/brasilprev/api/client/{cpf}", tags=["Cadastro de cliente"])
def read(cpf: str):
    client = ClientController()
    return client.read_client(cpf)

@router_client.put("/brasilprev/api/client/{cpf}", tags=["Cadastro de cliente"])
def update(cpf: str, metadata: MetadataClient):
    client = ClientController()
    return client.update_client(cpf, metadata.cpf, metadata.name, metadata.email, metadata.birthdate, metadata.gender, metadata.monthlyIncome)


@router_client.delete("/brasilprev/api/client/{cpf}", tags=["Cadastro de cliente"])
def delete(cpf: str):
    client = ClientController()
    return client.delete_client(cpf)