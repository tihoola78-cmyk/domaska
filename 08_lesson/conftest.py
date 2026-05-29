import pytest
from api_client import ApiClient
from project_api import ProjectAPI


@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


@pytest.fixture(scope="session")
def project_api(api_client):
    return ProjectAPI(api_client)


@pytest.fixture(scope="module")
def test_project_data():
    return {
        "title": "My Test Project",
    }


@pytest.fixture(scope="module")
def created_project_id(project_api, test_project_data):
    response = project_api.create_project(test_project_data)
    assert response.status_code == 201, f"Не удалось создать проект. Статус: {response.status_code}, Ответ: {response.text}"
    project_id = response.json().get("id")
    assert project_id is not None, "ID проекта не получен"
    yield project_id