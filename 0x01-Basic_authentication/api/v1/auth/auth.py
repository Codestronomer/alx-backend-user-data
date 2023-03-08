#!/usr/bin/env python3
"""Defines the auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage API authentication"""

    def __init__(self):
        """initializes class instances"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method for auth class
        Return:
            bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """public method for auth class
        Return:
            None type
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method for auth class
        Return:
            None type"""
        return None
