from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    email = "test.student@mergington.edu"

    # Arrange
    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Act
    unregister_response = client.delete(f"/activities/Chess Club/unregister?email={email}")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_unknown_participant_returns_not_found():
    # Act
    response = client.delete("/activities/Chess Club/unregister?email=missing@mergington.edu")

    # Assert
    assert response.status_code == 404
