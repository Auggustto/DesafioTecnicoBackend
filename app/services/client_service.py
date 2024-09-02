from app.models.client_models import ClientModels
from app.validators.client_validations import validation_cpf, validation_email
from app.validators.global_validation import convert_date


class ClientService:

    def create_client(self, cpf, name, email, birthdate, gender, monthlyIncome):
        if not all([cpf, name, email, birthdate, gender, monthlyIncome]):
            raise ValueError(
                "cpf, name, email, birthdate, gender, monthlyIncome are required!")

        validation_cpf(cpf)
        validation_email(email)
        date = convert_date(birthdate)

        client = ClientModels()
        return client.create(cpf, name, email, date, gender, monthlyIncome)

    def read_client(self, cpf):
        if not cpf:
            raise ValueError("cpf is required!")

        validation_cpf(cpf)

        client = ClientModels()
        return client.read(cpf)

    def update_client(self, cpf, new_cpf, name, email, birthdate, gender, monthlyIncome):
        if not all([cpf, new_cpf, name, email, birthdate, gender, monthlyIncome]):
            raise ValueError(
                "cpf, new_cpf, name, email, birthdate, gender, monthlyIncome are required!")

        validation_cpf(cpf)
        validation_email(email)
        date = convert_date(birthdate)

        client = ClientModels()
        return client.update(cpf, new_cpf, name, email, date, gender, monthlyIncome)

    def delete_client(self, cpf):
        if not cpf:
            raise ValueError("cpf is required!")

        validation_cpf(cpf)

        client = ClientModels()
        return client.delete(cpf)
