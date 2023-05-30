#!/usr/bin/env python3
"""Basic Authentication Implementation"""

import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """A Class that Implements Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """Returns the Base64 part of the `authorization` header
        for a Basic Authentication operation"""

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except base64.binascii.Error:
            return None
