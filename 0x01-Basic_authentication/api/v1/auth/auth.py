#!/usr/bin/env python3
"""
API authentication
"""
import requests
from typing import List, TypeVar


class Auth:
    """ Auth Class"""

    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ returns False """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            normalized_excluded_path = excluded_path if excluded_path.endswith('/') else excluded_path + '/'
            
            if normalized_excluded_path.endswith('*'):
                if normalized_path.startswith(normalized_excluded_path[:-1]):
                    return False
            elif normalized_path == normalized_excluded_path:
                return False

        return True
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
