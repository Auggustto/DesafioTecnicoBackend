from fastapi import FastAPI

from app.routers.client_routers import router_client
from app.routers.product_routers import router_product
from app.routers.plan_routers import router_plan
from app.routers.extra_contribution_routers import router_extra_ontribution
from app.routers.rescue_routes import router_rescue


app = FastAPI(title="API Brasilprev",
    description="Esta é a documentação da API construída com FastAPI, onde podemos testar as funcionalidades solicitadas no teste.",
    version="1.0.0"
    )

app.router.include_router(router_client)
app.router.include_router(router_product)
app.router.include_router(router_plan)
app.router.include_router(router_extra_ontribution)
app.router.include_router(router_rescue)


