import pytest


class TestProjectsAPI:
    @pytest.mark.positive
    def test_create_project(self, project_api, test_project_data):
        response = project_api.create_project(test_project_data)
        assert response.status_code == 201, f"Ошибка: {response.status_code}, {response.text}"
        assert "id" in response.json()

    @pytest.mark.positive
    def test_get_project(self, project_api, created_project_id):
        response = project_api.get_project(created_project_id)
        assert response.status_code == 200
        assert response.json().get("id") == created_project_id

    @pytest.mark.positive
    def test_update_project(self, project_api, created_project_id):
        updated_data = {"title": "Updated Name"}
        response = project_api.update_project(created_project_id, updated_data)
        assert response.status_code == 200

    @pytest.mark.negative
    def test_create_project_invalid_data(self, project_api):
        response = project_api.create_project({"wrong": "data"})
        assert response.status_code in [400, 422]

    @pytest.mark.negative
    def test_get_nonexistent_project(self, project_api):
        response = project_api.get_project("00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404

    @pytest.mark.negative
    def test_update_project_without_auth(self, api_client, created_project_id):
        # Сохраняем оригинальные заголовки
        original_headers = api_client.headers.copy()
        # Убираем авторизацию
        api_client.headers.pop("Authorization", None)
        response = api_client.put(f"/api-v2/projects/{created_project_id}", {"title": "x"})
        # Восстанавливаем заголовки
        api_client.headers = original_headers
        assert response.status_code == 401