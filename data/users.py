import os
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


def _password() -> str:
    value = os.getenv("SAUCE_PASSWORD")
    if not value:
        raise ValueError(
            "SAUCE_PASSWORD is not set. Copy .env.example to .env and fill it in.")
    return value


def standard_user() -> User:
    return User('standard_user', _password())


def locked_user() -> User:
    return User('locked_out_user', _password())


def problem_user() -> User:
    return User('problem_user', _password())
