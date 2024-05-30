#!/usr/bin/env python3
"""
Authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ a _hash_password method that takes in a password
    string arguments and returns bytes. """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    UUID = uuid4()
    return str(UUID)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Intializing """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a new user. """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user

        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ It should expect email and password required arguments and
        return a boolean."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        check = bcrypt.checkpw(password.encode(), user.hashed_password)
        if check:
            return True
        else:
            return False
