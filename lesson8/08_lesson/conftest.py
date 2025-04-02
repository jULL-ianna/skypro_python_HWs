import pytest
from utils.api_client import YougileClient


@pytest.fixture
def api_client():
    return YougileClient()


@pytest.fixture
def test_project(api_client):
    # Создаем тестовый проект
    response = api_client.create_project("Test Project")
    assert response.status_code == 201
    project_id = response.json()["id"]
    
    yield project_id  # Возвращаем ID проекта для тестов
    
    # Удаляем проект после тестов
    api_client.update_project(project_id, deleted=True)