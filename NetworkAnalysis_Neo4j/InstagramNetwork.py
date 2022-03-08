# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:30:12 2022

@author: nehkumar
"""

from Constants import *

import logging
from py2neo import Graph, Node, Relationship
from py2neo.matching import *
import traceback

class InstagramNetwork():
    """ Stores nodes and relations data in a graph database"""
    
    def __init__(self, args):
        """Instantiate Graph and NodeMatcher"""
        self.logger = logging.getLogger(__name__)
        self.graph = Graph(host=args.host, user=args.username, password=args.password)
        self.node_matcher = NodeMatcher(self.graph)
        
    def _populate_node(self, tx, node_name, node_labels):
        """Store node with its label"""
        node_exists = self.node_matcher.match(node_labels[0], name=node_name).exists()
        if node_exists:
            self.logger.info("Node: {} already exists".format(node_name))
        else:            
            self.logger.info("Creating node for user: {}".format(node_name))
            tx.create(Node(node_labels[0], node_labels[1], name=node_name))

    def populate_nodes(self, nodes):
        self.logger.info("Persist nodes in database...")
        tx = self.graph.begin()
        for name, label in nodes.items():
            if label in (BRAND, RETAILER, PUBLISHER, INFLUENCER):
                node_labels = (BEAUTY_ENTITY, label)
            else:
                node_labels = (NOT_BEAUTY_ENTITY, label)
            try:                
                self._populate_node(tx, name, node_labels)
            except Exception:
                self.logger.error("Exception persisting node with name: {} label: {}".format(name, label))
                traceback.print_exc()                
        tx.commit()
        
    
    def populate_edges(self, edges):
        """Store edge as a directed relation "SUGGESTED" """
        self.logger.info("Persist edges in database...")
        tx = self.graph.begin()
        for source, target in edges:
            try:
                source_node = self.node_matcher.match(BEAUTY_ENTITY, name=source).first()
                if source_node is None:
                    self.logger.error("Skipping relation b/w {} and {} as source node does not exist".format(source, target))
                    continue
                
                target_node = self.node_matcher.match(BEAUTY_ENTITY, name=target).first()
                if target_node is None:
                    target_node = self.node_matcher.match(NOT_BEAUTY_ENTITY, name=target).first()
                    if target_node is None:
                        self.logger.error("Skipping relation b/w {} and {} as target node does not exist".format(source, target))
                        continue
                        
                s_rel_t = Relationship(source_node, "SUGGESTED", target_node)
                tx.create(s_rel_t)
            except Exception:
                self.logger.error("Exception persisting edge between {} and {}".format(source, target))
                traceback.print_exc()
                
        tx.commit()
          
            
        
        
            
                
                
                
                
            
            
            
            
        
        
        
        
        
        