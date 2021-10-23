from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, Request
from typing import Optional

router = APIRouter(prefix='/private')


class Person(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None


@router.post('/')
def get(request: Request, person: Person, Authorize: AuthJWT = Depends()):
    print(request.client.host)
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"user": current_user, 'person': person}
