#!/usr/bin/env python3
"""
API session authentication
"""
from .auth import Auth
import requests
from typing import List, TypeVar
import base64
from models.user import User


class SessionAuth(Auth):
    """ Basic Auth inheriting from Auth"""
    pass
