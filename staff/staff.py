"""
File: staff.py
Description: Defines the staff class, representing staff members in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC


class Staff(ABC):
    """
    Abstract base class representing staff members in the zoo.
    Provides common attributes and methods for all staff members.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name):
        self._name = name
        self._animals = []
        self._enclosures = []
        self._job = None

    # ===============================
    #           PROPERTIES
    # ===============================

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @property
    def job(self):
        return self._job

    @property
    def enclosures(self):
        return self._enclosures

    # ===============================
    #           SETTERS
    # ===============================

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    @job.setter
    def job(self, job):
        self._job = job

    @enclosures.setter
    def enclosures(self, enclosures):
        self._enclosures = enclosures
