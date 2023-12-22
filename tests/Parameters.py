#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : # @Time    : 2023-12-22 16:55
# @Author  : Jack
# @File    : Parameters.py

from os import environ

"""
Parameters
"""


class Parameters:
    def __int__(self):
        pass

    def get(self, key, default=None, type=None, onlyEnv=True):
        """
            Returns the value from the key.
            First check environment variables.
            Second check request headers if "onlyEnv=False".
        """
        value = default

        if key in environ:
            value = environ.get(key)

        if (type is None) or (default is None):
            return value

        if type == bool:
            return value == "True"

        return type(value)
