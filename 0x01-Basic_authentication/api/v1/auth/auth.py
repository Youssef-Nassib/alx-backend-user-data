#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ return False-path"""
        return False

    def authorization_header(self, request=None) -> str:
        """return None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
