from tests.test_config import temp_db, client


@temp_db
def test_create_user():
    request_data = {
        "username": "string",
        "telegram_id": "string",
        "first_name": "string",
        "last_name": "string",
        "additional_information": "string"
    }
    response = client.post(
        url='/users/',
        json=request_data
    )
    assert response.status_code == 1