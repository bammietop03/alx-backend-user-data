#!/usr/bin/env python3
"""
API authentication
"""
from .auth import Auth
import requests
from typing import List, TypeVar
import base64
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth inheriting from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string
            base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header,
                                             validate=True)

            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from
            the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' in decoded_base64_authorization_header:
            separate = decoded_base64_authorization_header.split(':')
            return separate[0], separate[1]
        else:
            return None, None

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_email, str):
            return None

        users = User.search({'email': user_email})
        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        if request is None:
            return None

        base64_token = self.authorization_header(request)
        if base64_token is None:
            return None
        extract_token = self.extract_base64_authorization_header(base64_token)
        if extract_token is None:
            return None
        decoded_token = self.decode_base64_authorization_header(extract_token)
        if decoded_token is None:
            return None
        user_details = self.extract_user_credentials(decoded_token)
        if base64_token is (None, None):
            return None
        user_object = self.user_object_from_credentials(user_details[0],
                                                        user_details[1])
        if user_object is None:
            return None
        return user_object
