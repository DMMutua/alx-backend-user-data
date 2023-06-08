#!/usr/bin/env python3


import bcrypt


def _hash_password(password: str) -> bytes:
    """Generates a salted hash of the input password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    salt = bcrypt.gensalt()

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_pw
