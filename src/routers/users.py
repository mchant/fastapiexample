from fastapi import APIRouter
from fastapi import Depends, HTTPException, Request
from fastapi_jwt_auth import AuthJWT

router = APIRouter(prefix='/users')


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


# @router.get("/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}

@router.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
