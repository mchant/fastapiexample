from fastapi import FastAPI, Depends, HTTPException, Request
from .routers import users, auth, private
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse

metadata = {
    'title': "ChimichangApp",
    'description': """ChimichangApp API helps you do awesome stuff. 🚀

                      ## Items

                      You can **read items**.

                      ## Users

                      You will be able to:

                      * **Create users** (_not implemented_).
                      * **Read users** (_not implemented_).
                   """,
    'version': "0.0.1",
    'terms_of_service': "http://example.com/terms/",
    'contact': {
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    'license_info': {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
}

app = FastAPI(**metadata)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(private.router)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
