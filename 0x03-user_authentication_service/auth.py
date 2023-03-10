#!/usr/bin/env python3
"""
defines auth methods related to password hashing
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    method takes a password string and return hashed byte value
    """
    # encoded_pwd = bytes(password, 'utf-8')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        """Initialize auth class instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Saves a user to database using self._db and returns the
        User object

        Args:
            email(str) : user's email
            password(str) : user's password
        Return:
            User object on success, ValueError if user exists
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user
