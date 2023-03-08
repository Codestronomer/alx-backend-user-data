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
        """public method for auth class to check if path requires authentication

        Args:
            path (str): path to check
            excluded_paths (List[str]): list of paths that do not require
                authentication

        Return:
            bool: True if the path is not in excluded_paths, False otherwise
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        if not path.endswith("/"):
            path = path + "/"
        if path in excluded_paths:
            return False
        return True

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
