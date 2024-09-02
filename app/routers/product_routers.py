from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.product_controller import ProductController

router_product = APIRouter()


class MetadataProduct(BaseModel):
    name : str
    susep : str
    expirationDate : str
    minValueInitialContribution : float
    minValueExtraContribution : float
    entryAge : int
    exitAge : int
    initialRescueWaitingPeriod : int
    timeBetweenRescues : int


@router_product.post("/api/devel/desafioTecnicoBackend/product", tags=["Cadastro de produto"])
def create(metadata : MetadataProduct):
    
    product = ProductController()
    return product.create_product(metadata.name, metadata.susep, metadata.expirationDate, metadata.minValueInitialContribution, metadata.minValueExtraContribution, metadata.entryAge, metadata.exitAge, metadata.initialRescueWaitingPeriod, metadata.timeBetweenRescues)

@router_product.get("/api/devel/desafioTecnicoBackend/product/{id_product}", tags=["Cadastro de produto"])
def read(id_product: str):
    product = ProductController()
    return product.read_product(id_product)

@router_product.put("/api/devel/desafioTecnicoBackend/product/{id_product}", tags=["Cadastro de produto"])
def update(id_product: str, metadata: MetadataProduct):
    product = ProductController()
    return product.update_product(id_product, metadata.name, metadata.susep, metadata.expirationDate, metadata.minValueInitialContribution, metadata.minValueExtraContribution, metadata.entryAge, metadata.exitAge, metadata.initialRescueWaitingPeriod, metadata.timeBetweenRescues)


@router_product.delete("/api/devel/desafioTecnicoBackend/product/{id_product}", tags=["Cadastro de produto"])
def delete(id_product: str):
    client = ProductController()
    return client.delete_product(id_product)