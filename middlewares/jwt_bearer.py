from fastapi.security import HTTPBearer
from starlette.requests import Request
from utils.jwt_manager import create_token,valite_toke
from fastapi import HTTPException

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth =  await super().__call__(request)
        data = valite_toke(auth.credentials)

        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403,detail="Credenciales invalidas")