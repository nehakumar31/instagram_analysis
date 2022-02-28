# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:58:16 2021

@author: nehkumar
"""

import logging
from Processor import Processor
from Constants import *    #all patterns are specified in constants

class Classifier(Processor):
    """Class to filter/classify an Instagram Profile based on pattern matching rules"""
    def __init__(self):
        self.logger = logging.getLogger(__name__)        
    
    def _match(self, pattern, target):
        """helper function to match a given pattern in target"""
        matches = pattern.findall(target)
        if matches:
            self.logger.info("Matches: {}".format(matches))
            return True
        
        return False
    
    """helper functions to look for keywords in profile
        -biography
        -full name
        -external url
    """
    def _match_beauty(self, profile):
        if ( (self._match(BEAUTY_PATTERN, profile.get_biography())) or 
             (self._match(BEAUTY_PATTERN, profile.get_full_name()))
           ):

            return True
        
        return False
    
    def _match_retailer(self, profile):
        matches =  self._match(SHOP_PATTERN, profile.get_external_url()) or self._match(RETAILERS_PATTERN, profile.get_biography())  or self._match(RETAILERS_PATTERN, profile.get_full_name())
        matches = matches and self._match_beauty(profile)        
        
        return matches
        
    def _match_publisher(self, profile):
        matches = self._match(PUBLISHER_PATTERN, profile.get_biography()) or self._match(PUBLISHER_PATTERN, profile.get_full_name())
        matches = matches and self._match_beauty(profile)
            
        return matches 
    
    def _match_influencer(self, profile):
        matches = self._match(INFLUENCER_PATTERN, profile.get_biography()) or self._match(PUBLISHER_PATTERN, profile.get_full_name())
    
        return matches 
    
    #overriding abstract method
    def execute(self, filename, profile, data_loader):
        """run the classification
           enrich the profile data with classified category
           persist the data to be consumed by further steps"""
        classify_res = self._classify(profile)
        self.logger.info("Classification result: {}".format(classify_res.value))
        if classify_res in (ClassificationResult.BRAND, ClassificationResult.RETAILER, ClassificationResult.PUBLISHER, ClassificationResult.INFLUENCER):
            profile_json = profile.get_raw_profile()
            profile_json['profile']['classified_category'] = classify_res.value
            data_loader.persist(filename, profile_json)
            data_loader.mark_processed(filename)
        
        elif classify_res == ClassificationResult.NOT_BEAUTY:
            data_loader.mark_discard(filename) 
            
        else:
            data_loader.mark_manual(filename)  
        
    
    def _classify(self, profile):
        """Incremental rule checking unless a profile is classified. 
        If no pattern match, profile needs to be considered manually"""
        
        if (profile.get_business_category_name() not in BUSINESS_CATEGORY):
            self.logger.info("Discard profile: {} as business category does not match".format(profile.get_name))
            return ClassificationResult.NOT_BEAUTY
        
        if ( (profile.get_category_name()  is not None) and 
             (profile.get_category_name() not in CATEGORY_NAMES) ):
            self.logger.info("Discard profile: {} as category name does not match".format(profile.get_category_name()))
            return ClassificationResult.NOT_BEAUTY
        
        if ( (profile.get_category_enum() is not None) and 
            (profile.get_category_enum() not in CATEGORY_ENUMS) ):
            self.logger.info("Discard profile: {} as category enum does not match".format(profile.get_category_enum()))
            return ClassificationResult.NOT_BEAUTY
        #have more stricter checks before this as SHOP_PATTERN can be with other goods too. 
        
        if (self._match_publisher(profile)):
            return ClassificationResult.PUBLISHER
        
        if (self._match_retailer(profile)):
            return ClassificationResult.RETAILER        
              
        if (self._match_beauty(profile)):
            return ClassificationResult.BRAND
        
        if (self._match_influencer(profile)):
            return ClassificationResult.INFLUENCER
        
        return ClassificationResult.HANDLE_MANUALLY
        
        
