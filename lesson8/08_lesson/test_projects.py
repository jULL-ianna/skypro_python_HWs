import pytest
from utils.api_client import YougileClient


class TestProjects:
    """Тесты для работы с проектами Yougile API"""
    
    def test_create_project_positive(self, api_client):
        """Позитивный тест создания проекта"""
        response = api_client.create_project("New Project")
        assert response.status_code == 201
        assert "id" in response.json()
    
    def test_create_project_negative_missing_title(self, api_client):
        """Негативный тест создания проекта без названия"""
        response = api_client.create_project(title=None)
        assert response.status_code != 201
        assert "error" in response.json()
    
    def test_update_project_positive(self, api_client, test_project):
        """Позитивный тест обновления проекта"""
        response = api_client.update_project(
            project_id=test_project,
            title="Updated Project"
        )
        assert response.status_code == 200
        assert "id" in response.json()
    
    def test_update_project_negative_invalid_id(self, api_client):
        """Негативный тест обновления несуществующего проекта"""
        response = api_client.update_project(
            project_id="invalid-id-123",
            title="Updated Project"
        )
        assert response.status_code == 404
        assert "error" in response.json()
    
    def test_get_project_positive(self, api_client, test_project):
        """Позитивный тест получения проекта"""
        response = api_client.get_project(test_project)
        assert response.status_code == 200
        assert response.json()["id"] == test_project
    
    def test_get_project_negative_not_found(self, api_client):
        """Негативный тест получения несуществующего проекта"""
        response = api_client.get_project("non-existent-id-123")
        assert response.status_code == 404
        assert "error" in response.json()