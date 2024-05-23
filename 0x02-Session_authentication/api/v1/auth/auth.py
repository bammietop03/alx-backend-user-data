#!/usr/bin/env python3
"""
API authentication
"""
import requests
from typing import List, TypeVar
import os


class Auth:
    """ Auth Class"""

    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ returns False """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        path_length = len(path)
        if path_length == 0:
            return True

        slash_path = True if path[path_length - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            exc_length = len(exc)
            if exc_length == 0:
                continue

            if exc[exc_length - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:exc_length - 1]:
                    return False

        return True
        # if path is None:
        #     return True

        # if excluded_paths is None or len(excluded_paths) == 0:
        #     return True

        # normalized_path = path if path.endswith('/') else path + '/'

        # for N_path in excluded_paths:
        #     if N_path.endswith('/') and normalized_path == N_path:
        #         return False

        # return True

    def authorization_header(self, request=None) -> str:
        """ returns None - request will be the Flask request object"""
        if request is None:
            return None

        if not hasattr(request, 'headers'):
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
