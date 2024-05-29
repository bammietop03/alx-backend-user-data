#!/usr/bin/env python3
"""
Authentication
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ a _hash_password method that takes in a password
    string arguments and returns bytes. """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
