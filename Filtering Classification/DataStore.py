# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:19:12 2021

@author: nehkumar
"""

from Processor import Processor
from Constants import *
from DataLoader import DataLoader
from InstagramProfile import Media, Comment

import logging
from py2neo import Graph, Node, Relationship
#from py2neo.data import Relationship
from py2neo.matching import *
import traceback

class ProfileDataStore(Processor):
    """ Stores profile data in a graph database"""
    
    def __init__(self, host, username, password, mode):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialize graph database host: {}".format(host))
        self.graph = Graph(host=host, user=username, password=password)
        self.node_matcher = NodeMatcher(self.graph)
        self.mode = mode    
        
    def execute(self, filename, profile, data_loader):
        self.logger.info("Persist in database...")       
        tx = self.graph.begin()
        try:
            if(self.mode == Mode.PERSIST_BEAUTY_ENTITY.value): 
                self._construct_entity_node(tx, profile)            
            
            if(self.mode == Mode.PERSIST_MEDIA.value):
                self._construct_media_node(tx, profile)
            
            tx.commit()
            data_loader.mark_processed(filename)              
        except Exception as exc:
            self.logger.error("Exception persisting data for profile: {}".format(profile.get_name()))
            traceback.print_exc()
            tx.rollback()
            data_loader.mark_error(filename)        
            
        
    def _construct_entity_node(self, tx, profile): 
        username = profile.get_name()
        self.logger.info("Processing node: {}".format(username))
        properties = profile.get_properties()
        node_exists = self.node_matcher.match(BEAUTY_ENTITY, name=username).exists()
        print("Properties: {}".format(properties))
        if node_exists:
            self.logger.info("Beauty node: {} already exists".format(username))
        else:            
            self.logger.info("Creating beauty node for user: {}".format(username))
            tx.create(Node(BEAUTY_ENTITY, profile.get_classified_category(), name=profile.get_name(), **profile.get_properties()))
        
    def _construct_media_node(self, tx, profile):
        self.logger.info("Creating media for user: {}".format(profile.get_name()))
        for post in profile.get_media_posts():
            self.logger.info("Processing media: {}".format(post.get_shortcode()))
            post_node = Node(POST, post.get_type(), name=post.get_shortcode(), **post.get_properties())
            tx.create(post_node)
            
            #Look for owner of post to create a relationship
            post_owner = post.get_owner()
            self.logger.info("Looking for owner: {}".format(post_owner))
            post_owner_node = self.node_matcher.match(BEAUTY_ENTITY, name=post_owner).first()
            if post_owner_node is None:
                self.logger.error("Couldn't find owner: {} of media post: {}".format(post_owner, post.get_shortcode()))
                raise ValueError("Skipping media of this profile")
            
            self.logger.info("Owner node found: {}".format(post_owner_node))
            o_rel_p = Relationship(post_owner_node, "POSTED", post_node)
            tx.create(o_rel_p)
            
            (hashtags, tagged_usernames) = post.get_tags()
            self._create_hashtag_relation(tx, post_node, hashtags)                    
            self._create_tagged_user_relation(tx, post_node, tagged_usernames)                
            
            iter = 0
            for comment in post.get_comments():
                self.logger.info("Processing comment: {}".format(comment.get_id()))
                comment_node = Node(COMMENT, name=comment.get_id(), **comment.get_properties())
                tx.create(comment_node)
                
                p_rel_c = Relationship(post_node, "HAS_COMMENT", comment_node)
                tx.create(p_rel_c)
                
                (hashtags, tagged_usernames) = comment.get_tags()
                self._create_hashtag_relation(tx, comment_node, hashtags)                    
                self._create_tagged_user_relation(tx, comment_node, tagged_usernames)                
                
                comment_owner = comment.get_owner()
                comment_owner_node = self.node_matcher.match(BEAUTY_ENTITY, name=comment_owner).first()
                if comment_owner_node is None:
                    self.logger.info("Skipping comment owner relationship for comment: {} as owner: {} is not found".format(comment.get_id(), comment_owner))
                    continue    
                
                o_rel_c = Relationship(comment_owner_node, "COMMENTED", comment_node)
                tx.create(o_rel_c)
                
                iter += 1
                if (iter >= 5):    #for now limiting to 10 comments for each post
                    break
                
    def _create_hashtag_relation(self, tx, source_node, hashtags):
        for hashtag in hashtags:            
            #hashtag might be a beautity entity, so search for it
            hashtag = hashtag.lower()
            hashtag_node = self.node_matcher.match(BEAUTY_ENTITY, name=hashtag).first()
            if hashtag_node is None:
                #check for hashtag label nodes
                hashtag_node = self.node_matcher.match(HASHTAG, name=hashtag).first()
                
            if hashtag_node is None:
                hashtag_node = Node(HASHTAG, name=hashtag)
                tx.create(hashtag_node)
            
            s_rel_h = Relationship(source_node, "HAS_HASHTAG", hashtag_node)
            tx.create(s_rel_h)
            
    def _create_tagged_user_relation(self, tx, source_node, tagged_usernames):
        for tagged_username in tagged_usernames:
            tagged_user_node = self.node_matcher.match(BEAUTY_ENTITY, name=tagged_username).first()
            if tagged_user_node is None:
                self.logger.info("Tagged user: {} does not exist in network, so skipping".format(tagged_username))
                continue
            
            s_rel_t = Relationship(source_node, "HAS_TAGGED_USER", tagged_user_node)
            tx.create(s_rel_t)
            
                
                
                
                
            
            
            
            
        
        
        
        
        
        