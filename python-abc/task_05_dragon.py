#!/usr/bin/env python3
"""
This module defines mixins and a Dragon class to demonstrate
multiple inheritance using mixins.
"""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly."""

    def roar(self):
        print("The dragon roars!")
