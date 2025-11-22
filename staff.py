"""
File: staff.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC

from animal import Animal


# TODO Separate all classes into their own files.

class Staff(ABC):
    def __init__(self, name):
        self._name = name
        self._animals = []
        self._enclosures = []
        self._job = None

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job

    @property
    def enclosures(self):
        return self._enclosures

    @enclosures.setter
    def enclosures(self, enclosures):
        self._enclosures = enclosures






