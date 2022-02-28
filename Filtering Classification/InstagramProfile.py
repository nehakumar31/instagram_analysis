# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:47:48 2021

@author: nehkumar
"""

import json
import logging
import re
from Constants import *

def extract_hashtags_usernames(text):
    hashtags = re.findall(
            r"(?<!&)#(\w+|(?:[\xA9\xAE\u203C\u2049\u2122\u2139\u2194-\u2199\u21A9\u21AA\u231A\u231B\u2328\u2388\u23CF\u23E9-\u23F3\u23F8-\u23FA\u24C2\u25AA\u25AB\u25B6\u25C0\u25FB-\u25FE\u2600-\u2604\u260E\u2611\u2614\u2615\u2618\u261D\u2620\u2622\u2623\u2626\u262A\u262E\u262F\u2638-\u263A\u2648-\u2653\u2660\u2663\u2665\u2666\u2668\u267B\u267F\u2692-\u2694\u2696\u2697\u2699\u269B\u269C\u26A0\u26A1\u26AA\u26AB\u26B0\u26B1\u26BD\u26BE\u26C4\u26C5\u26C8\u26CE\u26CF\u26D1\u26D3\u26D4\u26E9\u26EA\u26F0-\u26F5\u26F7-\u26FA\u26FD\u2702\u2705\u2708-\u270D\u270F\u2712\u2714\u2716\u271D\u2721\u2728\u2733\u2734\u2744\u2747\u274C\u274E\u2753-\u2755\u2757\u2763\u2764\u2795-\u2797\u27A1\u27B0\u27BF\u2934\u2935\u2B05-\u2B07\u2B1B\u2B1C\u2B50\u2B55\u3030\u303D\u3297\u3299]|\uD83C[\uDC04\uDCCF\uDD70\uDD71\uDD7E\uDD7F\uDD8E\uDD91-\uDD9A\uDE01\uDE02\uDE1A\uDE2F\uDE32-\uDE3A\uDE50\uDE51\uDF00-\uDF21\uDF24-\uDF93\uDF96\uDF97\uDF99-\uDF9B\uDF9E-\uDFF0\uDFF3-\uDFF5\uDFF7-\uDFFF]|\uD83D[\uDC00-\uDCFD\uDCFF-\uDD3D\uDD49-\uDD4E\uDD50-\uDD67\uDD6F\uDD70\uDD73-\uDD79\uDD87\uDD8A-\uDD8D\uDD90\uDD95\uDD96\uDDA5\uDDA8\uDDB1\uDDB2\uDDBC\uDDC2-\uDDC4\uDDD1-\uDDD3\uDDDC-\uDDDE\uDDE1\uDDE3\uDDEF\uDDF3\uDDFA-\uDE4F\uDE80-\uDEC5\uDECB-\uDED0\uDEE0-\uDEE5\uDEE9\uDEEB\uDEEC\uDEF0\uDEF3]|\uD83E[\uDD10-\uDD18\uDD80-\uDD84\uDDC0]|(?:0\u20E3|1\u20E3|2\u20E3|3\u20E3|4\u20E3|5\u20E3|6\u20E3|7\u20E3|8\u20E3|9\u20E3|#\u20E3|\\*\u20E3|\uD83C(?:\uDDE6\uD83C(?:\uDDEB|\uDDFD|\uDDF1|\uDDF8|\uDDE9|\uDDF4|\uDDEE|\uDDF6|\uDDEC|\uDDF7|\uDDF2|\uDDFC|\uDDE8|\uDDFA|\uDDF9|\uDDFF|\uDDEA)|\uDDE7\uD83C(?:\uDDF8|\uDDED|\uDDE9|\uDDE7|\uDDFE|\uDDEA|\uDDFF|\uDDEF|\uDDF2|\uDDF9|\uDDF4|\uDDE6|\uDDFC|\uDDFB|\uDDF7|\uDDF3|\uDDEC|\uDDEB|\uDDEE|\uDDF6|\uDDF1)|\uDDE8\uD83C(?:\uDDF2|\uDDE6|\uDDFB|\uDDEB|\uDDF1|\uDDF3|\uDDFD|\uDDF5|\uDDE8|\uDDF4|\uDDEC|\uDDE9|\uDDF0|\uDDF7|\uDDEE|\uDDFA|\uDDFC|\uDDFE|\uDDFF|\uDDED)|\uDDE9\uD83C(?:\uDDFF|\uDDF0|\uDDEC|\uDDEF|\uDDF2|\uDDF4|\uDDEA)|\uDDEA\uD83C(?:\uDDE6|\uDDE8|\uDDEC|\uDDF7|\uDDEA|\uDDF9|\uDDFA|\uDDF8|\uDDED)|\uDDEB\uD83C(?:\uDDF0|\uDDF4|\uDDEF|\uDDEE|\uDDF7|\uDDF2)|\uDDEC\uD83C(?:\uDDF6|\uDDEB|\uDDE6|\uDDF2|\uDDEA|\uDDED|\uDDEE|\uDDF7|\uDDF1|\uDDE9|\uDDF5|\uDDFA|\uDDF9|\uDDEC|\uDDF3|\uDDFC|\uDDFE|\uDDF8|\uDDE7)|\uDDED\uD83C(?:\uDDF7|\uDDF9|\uDDF2|\uDDF3|\uDDF0|\uDDFA)|\uDDEE\uD83C(?:\uDDF4|\uDDE8|\uDDF8|\uDDF3|\uDDE9|\uDDF7|\uDDF6|\uDDEA|\uDDF2|\uDDF1|\uDDF9)|\uDDEF\uD83C(?:\uDDF2|\uDDF5|\uDDEA|\uDDF4)|\uDDF0\uD83C(?:\uDDED|\uDDFE|\uDDF2|\uDDFF|\uDDEA|\uDDEE|\uDDFC|\uDDEC|\uDDF5|\uDDF7|\uDDF3)|\uDDF1\uD83C(?:\uDDE6|\uDDFB|\uDDE7|\uDDF8|\uDDF7|\uDDFE|\uDDEE|\uDDF9|\uDDFA|\uDDF0|\uDDE8)|\uDDF2\uD83C(?:\uDDF4|\uDDF0|\uDDEC|\uDDFC|\uDDFE|\uDDFB|\uDDF1|\uDDF9|\uDDED|\uDDF6|\uDDF7|\uDDFA|\uDDFD|\uDDE9|\uDDE8|\uDDF3|\uDDEA|\uDDF8|\uDDE6|\uDDFF|\uDDF2|\uDDF5|\uDDEB)|\uDDF3\uD83C(?:\uDDE6|\uDDF7|\uDDF5|\uDDF1|\uDDE8|\uDDFF|\uDDEE|\uDDEA|\uDDEC|\uDDFA|\uDDEB|\uDDF4)|\uDDF4\uD83C\uDDF2|\uDDF5\uD83C(?:\uDDEB|\uDDF0|\uDDFC|\uDDF8|\uDDE6|\uDDEC|\uDDFE|\uDDEA|\uDDED|\uDDF3|\uDDF1|\uDDF9|\uDDF7|\uDDF2)|\uDDF6\uD83C\uDDE6|\uDDF7\uD83C(?:\uDDEA|\uDDF4|\uDDFA|\uDDFC|\uDDF8)|\uDDF8\uD83C(?:\uDDFB|\uDDF2|\uDDF9|\uDDE6|\uDDF3|\uDDE8|\uDDF1|\uDDEC|\uDDFD|\uDDF0|\uDDEE|\uDDE7|\uDDF4|\uDDF8|\uDDED|\uDDE9|\uDDF7|\uDDEF|\uDDFF|\uDDEA|\uDDFE)|\uDDF9\uD83C(?:\uDDE9|\uDDEB|\uDDFC|\uDDEF|\uDDFF|\uDDED|\uDDF1|\uDDEC|\uDDF0|\uDDF4|\uDDF9|\uDDE6|\uDDF3|\uDDF7|\uDDF2|\uDDE8|\uDDFB)|\uDDFA\uD83C(?:\uDDEC|\uDDE6|\uDDF8|\uDDFE|\uDDF2|\uDDFF)|\uDDFB\uD83C(?:\uDDEC|\uDDE8|\uDDEE|\uDDFA|\uDDE6|\uDDEA|\uDDF3)|\uDDFC\uD83C(?:\uDDF8|\uDDEB)|\uDDFD\uD83C\uDDF0|\uDDFE\uD83C(?:\uDDF9|\uDDEA)|\uDDFF\uD83C(?:\uDDE6|\uDDF2|\uDDFC))))[\ufe00-\ufe0f\u200d]?)+",
            text, re.UNICODE)
    hashtags = list(set(hashtags))
    
    tagged_usernames = re.findall(r'@([^\s+]+)', text)
    tagged_usernames = list(set(tagged_usernames))
    
    return(hashtags, tagged_usernames)   
    

class Comment:
    """ Class representing a comment of a media post """
    def __init__(self,  comment_data):
        self.comment = comment_data
        
    def get_id(self):
        return self.comment['node']['id']
    
    def get_owner(self):
        return self.comment['node']['owner']['username']
    
    def get_tags(self):
        text = self.comment['node']['text']
        return extract_hashtags_usernames(text)
    
    def creation_time(self):
        return self.comment['node']['created_at']
    
    def get_likedby_count(self):
        return self.comment['node']['edge_liked_by']['count']
    
    def get_text(self):
        return self.comment['node']['text']
    
    def get_properties(self):
        properties = { 'text':self.get_text(), 'likes':self.get_likedby_count(),
                'posted_time' : self.creation_time()            
                }
        return properties

class Media:
    """ Class representing a media post of a profile """
    def __init__(self, media_data):
        self.media = media_data

    def get_type(self):
        if self.media['__typename'] == 'GraphVideo':
            return MediaType.VIDEO.value
        elif self.media['__typename'] == 'GraphImage':
            return MediaType.IMAGE.value
        
        return None
    
    def get_shortcode(self):
        return self.media['shortcode']
    
    def get_owner(self):
        return self.media['owner']['username']
    
    def is_video(self):
        return (self.media['__typename'] == 'GraphVideo')
    
    def get_comments_count(self):
        return self.media['edge_media_to_comment']['count']
    
    def get_likedby_count(self):
        return self.media['edge_liked_by']['count']
    
    def get_video_view_count(self):
        if 'video_view_count' in self.media:
            return self.media['video_view_count']
        
        return None
    
    def get_text(self):
        caption_text = ''
        if 'caption' in self.media and self.media['caption']:
            if isinstance(self.media['caption'], dict):
                caption_text = self.media['caption']['text']
            else:
                caption_text = self.media['caption']

        elif 'edge_media_to_caption' in self.media and self.media['edge_media_to_caption'] and self.media['edge_media_to_caption']['edges']:
            caption_text = self.media['edge_media_to_caption']['edges'][0]['node']['text']
            
        return caption_text
    
    def get_tags(self):
        caption_text = ''
        if 'caption' in self.media and self.media['caption']:
            if isinstance(self.media['caption'], dict):
                caption_text = self.media['caption']['text']
            else:
                caption_text = self.media['caption']

        elif 'edge_media_to_caption' in self.media and self.media['edge_media_to_caption'] and self.media['edge_media_to_caption']['edges']:
            caption_text = self.media['edge_media_to_caption']['edges'][0]['node']['text']
            
        return extract_hashtags_usernames(caption_text)
        
    def creation_time(self):
        return self.media['taken_at_timestamp']
    
    def get_properties(self):
        properties = {'likes' : self.get_likedby_count(), 'comments_count' : self.get_comments_count(),
                      'posted_time' : self.creation_time(), 'text':self.get_text()}
        
        if self.is_video():
            properties['view_count'] = self.get_video_view_count()
        
        return properties
        
    def get_comments(self):
        """ A generator function to return media comments """
        if 'comments' in self.media and self.media['comments']:
            for comment_data in self.media['comments']:
                comment_item = Comment(comment_data)
                yield comment_item

        return            
        
    
class Profile:
    """Class representing InstagramProfile and corresponsing getter methods for same"""
    
    def __init__(self, profile_data):
        self.logger = logging.getLogger(__name__)
        self.profile = json.loads(profile_data)
        
    def get_name(self):
        if 'username' in self.profile['profile']:
            return self.profile['profile']['username']
        else:
            if 'media' in self.profile and self.profile['media']:
                return self.profile['media'][0]['owner']['username']

        return None  


    def get_id(self):
        return self.profile['profile']['id']
    
    def get_posts_count(self):
        return self.profile['profile']['posts_count']
    
    def get_followers_count(self):
        return self.profile['profile']['followers_count']
        
    def get_following_count(self):
        return self.profile['profile']['following_count']
    
    def get_media_posts(self):
        """ A generator function to return a media post """
        if 'media' in self.profile and self.profile['media']:
            for media_data in self.profile['media']:
                media_item = Media(media_data)
                yield media_item
        
        return
        
    
    def get_properties(self):
        return {'id':self.get_id(), 'posts':self.get_posts_count(),
                'followers':self.get_followers_count(), 
                'following':self.get_following_count()}   

    def get_raw_profile(self):
        return self.profile
    
    def get_classified_category(self):
        return self.profile['profile']['classified_category']
    
    def get_business_category_name(self):
        return self.profile['profile']['business_category_name']
    
    def get_external_url(self):
        return self.profile['profile']['external_url']
    
    def get_category_name(self):
        if 'category_name' in self.profile['profile']:
            return self.profile['profile']['category_name']
        
        return None
    
    def get_category_enum(self):
        if 'category_enum' in self.profile['profile']:
            return self.profile['profile']['category_enum']
        
        return None
    
    def get_biography(self):
        return self.profile['profile']['biography']
    
    def get_full_name(self):
        return self.profile['profile']['full_name']
    
    def is_complete(self):
        if 'media' in self.profile and self.profile['media']:
            if 'comments' in self.profile['media'][0]:
                return True
        
        return False