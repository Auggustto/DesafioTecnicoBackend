import uvicorn
from app import app

from app.models.database.new_database_models import *
from app.models.database.connect_database import engine, Base

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # uvicorn.run(app, host="localhost", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=80)
