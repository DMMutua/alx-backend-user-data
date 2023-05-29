#!/usr/bin/env python3
"""Implementation of Authentication Management"""


from flask import request
from typing import List, TypeVar


class Auth:
    """
    A Class to Manage SimpleAPI User Authentication.
    Implements Basic Access Authentication Protocol.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False for Now"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns `None` for Now"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns `None` for Now"""
        return None
