import requests
from configparser import ConfigParser

class APIClient:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("C:/Python selenium/BritsApiTask/Configurations/config.ini")
        self.base_url = self.config.get("API", "base_url")
        self.resource = self.config.get("API", "resource")
        self.query_param = self.config.get("API", "query_param")

    def patch(self, data, headers=None):
        url = f"{self.base_url}/{self.resource}/{self.query_param}"
        return requests.patch(url, json=data, headers=headers)