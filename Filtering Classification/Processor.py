# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from InstagramProfile import Profile
from DataLoader import DataLoader

class Processor(ABC):
    @abstractmethod
    def execute(self, filename, profile, data_loader):
        pass