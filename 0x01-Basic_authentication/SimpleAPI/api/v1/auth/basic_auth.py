#!/usr/bin/env python3
"""
API authentication
"""
from .auth import Auth
import requests
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Basic Auth inheriting from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split(' ')[1]
