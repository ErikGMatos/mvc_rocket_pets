from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.person_creator_view import PersonCreatorView

MOCK_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 23,
    "pet_id": 123
}


def test_handle(mocker):
    mock_controller = mocker.Mock()
    mock_controller.create.return_value = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": MOCK_USER
        }
    }
    view = PersonCreatorView(mock_controller)
    http_request = HttpRequest(body=MOCK_USER)
    response = view.handle(http_request)

    assert response.status_code == 200
    assert response.body == {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": MOCK_USER
        }
    }
    assert isinstance(response, HttpResponse)
    mock_controller.create.assert_called_once_with(MOCK_USER)
