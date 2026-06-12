class ProjectAPI:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_project(self, project_data):
        response = self.api_client.post("/projects", project_data)
        return response

    def update_project(self, project_id, project_data):
        endpoint = f"/projects/{project_id}"
        response = self.api_client.put(endpoint, project_data)
        return response

    def get_project(self, project_id):
        endpoint = f"/projects/{project_id}"
        response = self.api_client.get(endpoint)
        return response