import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_natural_language():
    response = client.post("/api/process_natural_language", data={"description": "Create an API for tasks"})
    assert response.status_code == 200
    assert "api_spec" in response.json()

def test_healthcheck_postgresql():
    response = client.get("/api/healthcheck/postgresql")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_healthcheck_mongodb():
    response = client.get("/api/healthcheck/mongodb")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_healthcheck_openai():
    response = client.get("/api/healthcheck/openai")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

