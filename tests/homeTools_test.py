#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023-12-22 17:39
# @Author  : Jack
# @File    : homeTools_test.py

"""
homeTools_test
"""
from src import homeTools

if __name__ == '__main__':
    # print(homeTools.getRandomId())

    coords = ((0., 0.), (0., 1.), (1., 1.), (1., 0.), (0., 0.))
    print(homeTools.getBounds(coords))
