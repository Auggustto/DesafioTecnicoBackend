from fastapi import HTTPException
from app.services.client_service import ClientService

class ClientController:
    def __init__(self):
        self.client_service = ClientService()

    def create_client(self, cpf, name, email, birthdate, gender, monthlyIncome):
        try:
            return self.client_service.create_client(cpf, name, email, birthdate, gender, monthlyIncome)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def read_client(self, cpf):
        try:
            return self.client_service.read_client(cpf)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_client(self, cpf, new_cpf, name, email, birthdate, gender, monthlyIncome):
        try:
            return self.client_service.update_client(cpf, new_cpf, name, email, birthdate, gender, monthlyIncome)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def delete_client(self, cpf):
        try:
            return self.client_service.delete_client(cpf)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
