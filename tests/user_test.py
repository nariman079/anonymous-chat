from tests.test_config import client


def test_create_telegram_user():
    request_data = {
        "username": "string",
        "telegram_id": "string",
        "first_name": "string",
        "last_name": "string",
        "additional_information": "string"
    }

    response = client.post('/users/telegram_users/', json=request_data)
    assert response.status_code == 500
