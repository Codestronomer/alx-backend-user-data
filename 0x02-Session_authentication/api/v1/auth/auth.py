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
        """public method for auth class to check if path requires
            authentication

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
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method for auth class to validate all requests to secure
            the API

        Args:
            request: the request object
        Return:
            None: if request is None or doesn't contain the Authorization key
            Value of authorization header
        """
        if request is None:
            return None
        header = request.headers.get('Authorizaion')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """public method for auth class
        Return:
            None type"""
        return None
