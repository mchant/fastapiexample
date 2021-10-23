from fastapi import Depends, HTTPException, Request
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from fastapi import APIRouter

router = APIRouter(prefix='/auth')

class User(BaseModel):
    username: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"

@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/login')
def login(user: User, request: Request, Authorize: AuthJWT = Depends()):
    print(request.client.host, user.username, user.password)
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}

@router.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
