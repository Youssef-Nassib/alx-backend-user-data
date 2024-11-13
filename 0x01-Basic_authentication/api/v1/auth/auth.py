#!/usr/bin/env python3
"""Authentication module.
"""
from flask import request
from typing import List, TypeVar
import fnmatch
User = TypeVar('User')


class Auth:
    """Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths
            that do not require authentication.
        Returns:
            bool: returns False "not execluded_paths=len(excluded_paths)=0.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        Args:
            request: The Flask request object (default is None).
        Returns:
            str: None, as a placeholder for the authorization header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user associated with the request.
        Args:
            request: The Flask request object (default is None).
        Returns:
            TypeVar('User'): None, as a placeholder for the current user.
        """
        return None
