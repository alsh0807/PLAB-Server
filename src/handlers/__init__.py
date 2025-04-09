from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_405_METHOD_NOT_ALLOWED

from src.schemas import BaseResponse
from fastapi.encoders import jsonable_encoder


def add_validation_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def invalid_token_handler(request: BaseModel, exc: RequestValidationError):
        return JSONResponse(status_code=422, content=BaseResponse(message="토큰이 잘못되었습니다.").to_dict())

    @app.exception_handler(StarletteHTTPException)
    async def starlette_http_exception_handler(request: BaseModel, exc: StarletteHTTPException):
        message: str = exc.detail

        if exc.status_code == HTTP_405_METHOD_NOT_ALLOWED:
            message="허용되지 않은 메소드입니다."


        return JSONResponse(
            status_code=exc.status_code,
            content=BaseResponse(
                message=message
            ).to_dict()
        )
