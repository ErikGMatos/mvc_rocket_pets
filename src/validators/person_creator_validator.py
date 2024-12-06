from pydantic import BaseModel, ValidationError, constr

from src.errors.error_types.http_unprocessable import \
    HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest


def person_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: constr(min_length=1)  # type: ignore
        last_name: constr(min_length=1)  # type: ignore
        age: int  # age: int = None // in case I want to make it optional
        pet_id: int

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
