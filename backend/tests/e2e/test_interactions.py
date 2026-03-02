"""End-to-end tests for interactions endpoints."""

import os
import requests


def test_get_interactions_returns_200():
    base_url = os.getenv("API_BASE_URL")
    token = os.getenv("API_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{base_url}/interactions/", headers=headers)
    assert response.status_code == 200


def test_get_interactions_response_is_a_list():
    base_url = os.getenv("API_BASE_URL")
    token = os.getenv("API_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{base_url}/interactions/", headers=headers)
    data = response.json()
    assert isinstance(data, list)
