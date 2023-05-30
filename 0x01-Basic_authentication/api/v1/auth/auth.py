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
        """Method that checks whether a certain `path` is accessible.
        Leverages a List of `excluded_paths` for special cases.
        Returns:
            `True` if auth is required.`False` if otherwise.
        """
        
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        
        if path is None:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        
        return True


    def authorization_header(self, request=None) -> str:
        """Checks whether an Authorization Header Exists
        in the `request` object header.
        Returns:
            - The Value of the header if it exists.
            - None if Otherwise.
        """

        if request:
            if 'Authorization' not in request.headers:
                return None
            else:
                return request.headers['Authorization']


        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns `None` for Now"""
        return None
