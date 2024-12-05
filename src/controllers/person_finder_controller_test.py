from src.models.sqlite.entities.people import PeopleTable
from src.controllers.person_finder_controller import PersonFinderController


class MockPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPeopleRepository:
    def get_person(self, person_id: int) -> PeopleTable:  # pylint: disable=unused-argument
        return MockPerson(
            first_name="John",
            last_name="Doe",
            pet_name="Fluffy",
            pet_type="cat",
        )


def test_find():
    person_id = 123
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(person_id)

    expected_response = {
        "data": {
            "type": "Person"
            "count: 1",
            "attributes": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "pet_name": "Fluffy",
                    "pet_type": "cat"
            }
        }
    }

    assert response == expected_response
