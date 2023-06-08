#!/usr/bin/env python3


import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class Auth:
    """An Authentication Class for DB class"""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user and returns the User object.
        Returns User Object
        Raises:
            ValueError: If a user already exists with the passed email.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        except InvalidRequestError:
            pass

        hashed_pw = self._hash_password(password)
        user = self._db.add_user(email=email,
                                 hashed_password=hashed_pw)
        return user

    @staticmethod
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

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a login attempt.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(password.encode('utf-8'),
                                       user.hashed_password):
                return True
        except NoResultFound:
            pass

        except InvalidRequestError:
            pass

        return False

    @staticmethod
    def _generate_uuid() -> str:
        """Generates a new UUID and returns it as a string representation.

        Returns:
            str: The string representation of the generated UUID.
        """
        return str(uuid.uuid4())
