# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:04:03 2021

@author: nehkumar
"""

import re
from enum import Enum

class ClassificationResult(Enum):
    BRAND = "Brand"
    RETAILER = "Retailer"
    PUBLISHER = "Publisher"
    INFLUENCER = "Influencer"
    NOT_BEAUTY = "Not_A_Beauty_Entity"
    HANDLE_MANUALLY = "Manual_Classification"

class Mode(Enum):   
    CLASSIFY = 0,
    PERSIST_BEAUTY_ENTITY = 1
    PERSIST_MEDIA = 2
    
class MediaType(Enum):
    IMAGE = 'Image'
    VIDEO = 'Video'

BEAUTY_ENTITY = "BeautyEntity"
POST = "Post"
COMMENT = "Comment"
HASHTAG = "Hashtag"

#Patterns for profile classification
BUSINESS_CATEGORY=["Personal Goods & General Merchandise Stores",'Lifestyle Services',"Home Services", "Publisher","Publishers","Food & Personal Goods","Creators & Celebrities"]
SHOP_PATTERN=re.compile(r"\blikeshop\b", flags=re.IGNORECASE)
CATEGORY_NAMES=["Beauty, cosmetic & personal care","Food & Personal Goods","Health/beauty","Artist","Cosmetics store", "Brand","E-commerce website","Magazine","Makeup Artist"]
CATEGORY_ENUMS=["HEALTH_BEAUTY", 'COSMETICS_BEAUTY_SUPPLY','SPA_BEAUTY_PERSONAL_CARE','PRODUCT_SERVICE',"MAGAZINE","ARTIST","COSMETICS_BEAUTY_SUPPLY","ECOMMERCE_WEBSITE","MAKEUP_ARTIST","SKIN_CARE_SERVICES"]

BEAUTY_PATTERN = re.compile(r'Beauty|Look|cruelty-free|crueltyfree|Makeup|Cosmetics|Make Up', flags=re.IGNORECASE)
RETAILERS_PATTERN = re.compile(r'Shop', flags=re.IGNORECASE)
PUBLISHER_PATTERN = re.compile(r'Expert|Magazine|Tutorial|Tutorials', flags=re.IGNORECASE)
INFLUENCER_PATTERN = re.compile(r'Make\s*up\s*artist', flags=re.IGNORECASE)


    
    