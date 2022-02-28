# -*- coding: utf-8 -*-

from Classifier import Classifier
from DataStore import ProfileDataStore

class ProcessorFactory:
    """A factory method to fetch the processing needed based on mode"""
    def get_processor(self, args):
        if args.mode == 0:
            """run application in filtering and classification mode"""
            return Classifier()
        elif args.mode in (1,2):
            """run application in data store mode"""
            if (args.username is None) or (args.password is None): 
                raise ValueError("For datastore mode, username and password are mandatory args")
            
            return ProfileDataStore(args.host, args.username, args.password, args.mode)
        else: 
            raise ValueError("Invalid mode: {} for processing".format(args.mode))