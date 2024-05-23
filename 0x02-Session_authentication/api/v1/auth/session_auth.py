#!/usr/bin/env python3
"""
API session authentication
"""
from .auth import Auth
import requests
from typing import List, TypeVar
import base64
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Basic Auth inheriting from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id