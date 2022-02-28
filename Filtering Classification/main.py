# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:59:29 2021

@author: nehkumar
"""

#import os
import logging
import logging.config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("filtering_classification.log"),
        logging.StreamHandler()
    ]
)

import sys
import argparse
import json
from DataLoader import DataLoader
from InstagramProfile import Profile
from ProcessorFactory import ProcessorFactory
from Constants import *

def init_logging(work_dir, level = logging.DEBUG):
    logger = logging.getLogger()
    fh = logging.FileHandler(work_dir + '/classification.log')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    fh.setLevel(level)
    logger.addHandler(fh)

    #sh = logging.StreamHandler(sys.stdout)
    #sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    #sh.setLevel(logging.ERROR)
    #logger.addHandler(sh)
    return logger

def main():    
    print("Argument parsing....")
    parser = argparse.ArgumentParser(description=("Arguments to start Instagram profile filtering and classification"))
    parser.add_argument("--work-dir", "--work_dir", default='./', help="directory to read profiles from")
    parser.add_argument("--host", "--host", default=None, help="host to connect neo4j server if running in profile data store mode")
    parser.add_argument("--username", "--username", default=None, help="username to connect to graph database")
    parser.add_argument("--password", "--password", default=None, help="password to connect to graph database")
    parser.add_argument("--mode", "--mode", type=int, default=0, help="0- to only classify entity, 1- to store only beauty entities, 2- to store media as well")
    
    args = parser.parse_args()
    logger = logging.getLogger(__name__)
    logger.info("Instantiate...")
    
    processor = None
    factory = ProcessorFactory()
    try:
        processor = factory.get_processor(args)        
    except Exception as exc:
        logger.error(exc)
        parser.print_help()
        sys.exit(1)
    
    data_loader = DataLoader(args.work_dir)
    
    logger.info("Start processing...")       
    for file_detail in data_loader.get_profile_data():
        try:                
            logger.info("Processing file: {}".format(file_detail['file_name']))
            profile = Profile(file_detail['file_content'])
            
            processor.execute(file_detail['file_name'], profile, data_loader) 
         
        except Exception as exc:
            logger.error("Exception: {}".format(exc))
            data_loader.mark_error(file_detail['file_name'])     
        
    data_loader.backup_files()        
    logger.info("Application exiting...")    
    
if __name__ == '__main__':
    main()