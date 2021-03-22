import json


def test_fibonacci_five(test_client):
    test_request_payload = {"number": 5}
    test_response_payload = "[0, 1, 1, 2, 3, 5]"

    response = test_client.post("/fibonacci/", data=json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_fibonacci_zero(test_client):
    test_request_payload = {"number": 0}
    test_response_payload = "[0]"

    response = test_client.post("/fibonacci/", data=json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_fibonacci_negative(test_client):
    test_request_payload = {"number": -1}
    test_response_payload = {"detail": "Numbers must be at least 0"}
    response = test_client.post("/fibonacci/", data=json.dumps(test_request_payload), )

    assert response.status_code == 422
    assert response.json() == test_response_payload
