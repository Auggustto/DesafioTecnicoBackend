import logging
from fastapi import HTTPException

from app.models.database.connect_database import db
from app.models.database.new_database_models import  Client
from app.validators.global_validation import generator_id


class ClientModels:

    def filter_id_client(self, id_client):
        try:
            return db.query(Client).filter_by(id_client=id_client).first()
        except Exception as e:
            logging.error({"check_client_error": e})
            raise HTTPException(
                status_code=500, ddetail="Internal Server Error")

    def check_client(self, cpf):
        try:
            return db.query(Client).filter_by(cpf=cpf).first()
        except Exception as e:
            logging.error({"check_client_error": e})
            raise HTTPException(
                status_code=500, ddetail="Internal Server Error")

    def create(self, cpf, name, email, birthdate, gender, monthlyIncome):
        try:
            check_client = self.check_client(cpf)
            if check_client:
                raise HTTPException(
                    status_code=400, detail=f"CPF {cpf} is already in use!")

            id_client = generator_id()
            new_client = Client(cpf=cpf, name=name, email=email, birthdate=birthdate,
                                gender=gender, monthlyIncome=monthlyIncome, id_client=id_client)
            db.add(new_client)
            db.commit()

            return {"id": id_client}

        except HTTPException as e:
            logging.error({"create_client_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"create_client_error": e})
            raise

    def read(self, cpf):
        try:
            check_client = self.check_client(cpf)
            if check_client:
                return {
                    "cpf": check_client.cpf,
                    "name": check_client.name,
                    "email": check_client.email,
                    "birthdata": check_client.birthdate.strftime("%d/%m/%Y"),
                    "gender": check_client.gender,
                    "monthlyIncome": check_client.monthlyIncome,
                    "id_client": check_client.id_client,
                }
            raise HTTPException(
                status_code=400, detail=f"CPF {cpf} not found.")

        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"read_client_error": e})
            raise

    def update(self, cpf, new_cpf, name, email, birthdate, gender, monthlyIncome):
        try:
            check_client = self.check_client(cpf)
            if check_client:
                check_client.cpf = new_cpf
                check_client.name = name
                check_client.email = email
                check_client.birthdate = birthdate
                check_client.gender = gender
                check_client.monthlyIncome = monthlyIncome
                db.commit()

                return {"message": "User updated successfully!"}

            raise HTTPException(
                status_code=400, detail=f"CPF {cpf} not found.")

        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"read_client_error": e})
            raise

    def delete(self, cpf):
        try:
            check_client = self.check_client(cpf)
            if check_client:
                db.delete(check_client)
                db.commit()

                return {"message": f"CPF {cpf} deleted successfully!"}
            raise HTTPException(
                status_code=400, detail=f"CPF {cpf} not found.")

        except HTTPException as e:
            logging.error({"read_client_error": e.detail})
            raise e

        except Exception as e:
            logging.error({"read_client_error": e})
            raise
