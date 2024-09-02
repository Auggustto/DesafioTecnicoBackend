import pytest
from fastapi.testclient import TestClient
import sys
import os

test_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(test_dir)
sys.path.insert(0, project_dir)

from main import app


"""
    Teste criação de clientes
    
    deu boa 
"""

@pytest.fixture
def client():
    return TestClient(app)


def test_redirect_to_docs(client):
    response = client.get("/")
    assert response.status_code == 200


# @pytest.fixture
def test_create_client(client):
    payload = {
        "cpf": "12345678907",
        "name": "Leonardo",
        "email": "leo@example.com",
        "birthdate": "01/01/1990",
        "gender": "Masculino",
        "monthlyIncome": 5000
    }
    response = client.post("/brasilprev/api/client", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()
    return response.json()["id"]


def test_update_client(client):
    cpf = "12345678900"
    updated_payload = {
        "cpf": cpf,
        "name": "Updated Name",
        "email": "updated@example.com",
        "birthdate": "01/01/1990",
        "gender": "female",
        "monthlyIncome": 6000.0
    }
    response = client.put(f"/brasilprev/api/client/{cpf}", json=updated_payload)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json() == {"message": "User updated successfully!"}


@pytest.fixture
def test_read_client(client):
    cpf = "12345678900"
    response = client.get(f"/brasilprev/api/client/{cpf}")
    assert response.status_code == 200
    assert response.json()["cpf"] == cpf
    return response.json()["id_client"]
    
    

# def test_delete_client(client):
#     cpf = "12345678900"
#     response = client.delete(f"/brasilprev/api/client/{cpf}")
#     assert response.status_code == 200
#     assert response.json() == {"message": f"CPF {cpf} deleted successfully!"}



""" 
    Teste criação de produtos
    
    deu boa
"""

@pytest.fixture
def test_create_product(product):
    payload = {
        "name" : "Brasilprev Longo Prazo 20000034",
        "susep" : "15414900840201817",
        "expirationDate" : "10/06/2024",
        "minValueInitialContribution" : 1000,
        "minValueExtraContribution" : 100,
        "entryAge" : 18,
        "exitAge" : 60,
        "initialRescueWaitingPeriod" : 60,
        "timeBetweenRescues" : 30
    }
    response = product.post("/brasilprev/api/product", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()
    return response.json()["id"]


@pytest.fixture
def test_read_product(product, test_create_product):
    response = product.get(f"/brasilprev/api/product/{test_create_product}")
    assert response.status_code == 200
    assert response.json()["id_product"] == test_create_product
    return response.json()["id_product"]

@pytest.fixture
def test_update_product(product, test_read_product):
    payload = {
        "name" : "Brasilprev teste update",
        "susep" : "15414900840201817",
        "expirationDate" : "10/05/2024",
        "minValueInitialContribution" : 3000,
        "minValueExtraContribution" : 100,
        "entryAge" : 18,
        "exitAge" : 60,
        "initialRescueWaitingPeriod" : 60,
        "timeBetweenRescues" : 30
    }
    response = product.put(f"/brasilprev/api/product/{test_read_product}", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Product updated successfully!"


# def test_delete_product(product, test_read_product):
#     response = product.delete(f"/brasilprev/api/product/{test_read_product}")
#     assert response.status_code == 200
#     assert response.json()["message"] == f"ID {test_read_product} deleted successfully!"


"""
    Teste de criação de plano, esse teste depende das informações (id) de cliente e produto
    
    deu boa
"""
@pytest.fixture
def test_create_plan(product, test_read_client, test_create_product):
    payload = {
        "clientId" : test_read_client,
        "productId" : test_create_product,
        "contribution" : 1500,
        "retirementAge" : 60
    }
    response = product.post("/brasilprev/api/plan", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()
    return response.json()["id"]
    

def test_read_plan(product, test_create_plan):
    response = product.get(f"/brasilprev/api/plan/{test_create_plan}")
    assert response.status_code == 200
    assert response.json()["id_product"] == test_create_plan
    
    
"""
    Teste de criação de contribuição extra, esse teste depende das informações (id) de cliente e plan
    
    deu boa
"""
@pytest.fixture
def test_create_extra_contribution(product, test_read_client, test_create_plan):
    payload = {
    "ClientId" : test_read_client,
    "planId" : test_create_plan,
    "contributionValue" : 100
    }
    response = product.post("/brasilprev/api/plan/extra_contribution", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()
    return response.json()["id"]

def test_read_extra_contribution(product, test_create_extra_contribution):
    response = product.get(f"/brasilprev/api/plan/extra_contribution/{test_create_extra_contribution}")
    assert response.status_code == 200
    assert response.json()["id_extra_contribution"] == test_create_extra_contribution
    

"""
    Teste de resgate, esse teste depende das informações (id) de cliente e plan
    
    deu boa
"""
@pytest.fixture
def test_create_rescue(product, test_read_client, test_create_plan):
    payload = {
        "planId": test_create_plan,
        "clientId": test_read_client,
        "rescueValue": 50
    }
    response = product.post("/brasilprev/api/plan/rescue", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()
    return response.json()["id"]


def test_read_rescue(product, test_create_rescue):
    response = product.get(f"/brasilprev/api/plan/rescue/{test_create_rescue}")
    assert response.status_code == 200
    assert response.json()["id_rescue"] == test_create_rescue