from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities(monkeypatch):
    initial_activities = deepcopy(app_module.activities)
    monkeypatch.setattr(app_module, "activities", deepcopy(initial_activities))


@pytest.fixture
def client():
    return TestClient(app_module.app)
