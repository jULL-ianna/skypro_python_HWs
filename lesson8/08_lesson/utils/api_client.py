import requests
from utils.config import Config


class YougileClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {Config.AUTH_TOKEN}"
        }

    def create_project(self, title, users=None):
        url = f"{self.base_url}/projects"
        payload = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(url, json=payload, headers=self.headers)

    def update_project(self, project_id, title=None, users=None, deleted=None):
        url = f"{self.base_url}/projects/{project_id}"
        payload = {}
        if title:
            payload["title"] = title
        if users:
            payload["users"] = users
        if deleted is not None:
            payload["deleted"] = deleted
        return requests.put(url, json=payload, headers=self.headers)

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        return requests.get(url, headers=self.headers)