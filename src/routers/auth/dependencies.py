from typing import Any

from fastapi import Depends, Request
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.routers.auth.exceptions import InvalidToken, AccessTokenRequired, RefreshTokenRequired
from src.services.user import UserService
from src.routers.auth.utils import decode_token
from src.schemas.user import RefreshRequest

user_service = UserService()


def token_valid(token: str) -> bool:
    token_data = decode_token(token)

    return token_data is not None


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=False):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        creds = await super().__call__(request)

        if creds is None:
            raise InvalidToken()

        token = creds.credentials

        token_data = decode_token(token)

        if not token_valid(token):
            raise InvalidToken()

        self.verify_token_data(token_data)

        return token_data

    def verify_token_data(self, token_data: Any):
        raise NotImplementedError


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise AccessTokenRequired()


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: RefreshRequest) -> None:
        if token_data and not token_data.refresh_token:
            raise RefreshTokenRequired()


async def get_current_user(
    token_details: dict = Depends(AccessTokenBearer()),
    session: AsyncSession = Depends(get_session),
):
    user_email = token_details["user"]["email"]

    user = await user_service.get_user_by_email(user_email, session)

    return user