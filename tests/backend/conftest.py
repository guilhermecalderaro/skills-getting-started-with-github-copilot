import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as app_activities


INITIAL_ACTIVITIES = copy.deepcopy(app_activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_activities.clear()
    app_activities.update(copy.deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
