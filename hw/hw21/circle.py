#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = math.pi * radius ** 2

    def _get_d(self):
        return self._diamter

    def _set_d(self, value):
        self.diamater = value
        self.radius = value / 2
        self.area = math.pi * self.radius ** 2

    def _del_d(self):
        del self._diameter

    diamater = property(_get_d, _set_d, _del_d)
    doc = "largest distance between any two points on a circle"
