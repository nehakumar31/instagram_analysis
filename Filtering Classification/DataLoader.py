# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:06:59 2021

@author: nehkumar
"""

import glob
import os
import logging
import codecs
import json

class DataLoader:
    """fetch all file names from work directory and return content of one file each through a 
    generator function"""
    
    def __init__(self, work_dir):
        """Store all profile names in a list"""
        self.logger = logging.getLogger(__name__)
        self.work_dir = work_dir
        self.file_names = glob.glob(work_dir + '/*.json')        
        self.processed = []
        self.discard = []
        self.manual = []
        self.error = []
    
    
    def get_profile_data(self):
        """ A generator function iterating over files"""
        for file_name in self.file_names:
            self.logger.info("Loading file: {}".format(file_name))
            file_content = ''
            with open(file_name, 'r', encoding="utf-8") as file_handle:            
                file_content = file_handle.read()
            
            file_detail = {'file_name':file_name, 'file_content':file_content}
            yield file_detail
            
    def persist(self, file_name, file_content):    
        """All profiles classified as beauty entities will move to dir classified"""
        dest = self.work_dir + '\\classified\\'
        if not os.path.isdir(dest):
            os.makedirs(dest)
        
        file_basename = os.path.basename(file_name)
        with open(dest + file_basename, 'wb') as file_handle:
            self.logger.info("Moving profile: {} to classified".format(file_basename))
            json.dump(file_content, codecs.getwriter('utf-8')(file_handle), indent=4, sort_keys=True, ensure_ascii=False)
            
    def mark_processed(self, file_name):
        """Keeping a backup of classified profiles under dir Processed"""
        self.processed.append(file_name)
        
    def mark_discard(self, file_name):
        """Profiles - not a a beauty entity"""
        self.discard.append(file_name)

    def mark_manual(self, file_name):
        """Profiles that need manual intervention for classification"""
        self.manual.append(file_name)
        
    def mark_error(self, file_name):
        """Profiles whose data was erroneous"""
        self.error.append(file_name)
        
    def _move_files(self, file_names, target_dir):
        """helper function to move files"""
        for file_name in file_names:
            os.rename(file_name, target_dir + '\\' + os.path.basename(file_name))
            
    def backup_files(self):        
        if not os.path.isdir(self.work_dir + '\\processed\\'):
            os.makedirs(self.work_dir + '\\processed\\')
            
        if not os.path.isdir(self.work_dir + '\\discard\\'):
            os.makedirs(self.work_dir + '\\discard\\')
            
        if not os.path.isdir(self.work_dir + '\\manual\\'):
            os.makedirs(self.work_dir + '\\manual\\')
            
        if not os.path.isdir(self.work_dir + '\\error\\'):
            os.makedirs(self.work_dir + '\\error\\')
            
        self._move_files(self.processed, self.work_dir + 'processed')
        self._move_files(self.discard, self.work_dir + 'discard')
        self._move_files(self.manual, self.work_dir + 'manual')
        self._move_files(self.error, self.work_dir + 'error')
            
        
            
        
            
            
            
        
        