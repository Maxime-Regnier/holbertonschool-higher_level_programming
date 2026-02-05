#!/usr/bin/env python3
"""Abstract Base Class example with Animal, Dog, and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound."""
        pass


class Dog(Animal):
    """Dog class inherits from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class inherits from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
