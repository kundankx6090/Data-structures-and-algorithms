# -*- coding: utf-8 -*-
"""
Created on Sun May 29 07:57:39 2022

@author: kundan
"""

class Graph:
    def __init__(self):
        self.adjlist = {}
        
    def add_vertices(self,v):
        if v not in self.adjlist.keys():
            self.adjlist[v]=[]
            return True
        
        return False
            
    def remove_vertics(self,v):
        if v in self.adjlist.keys():
            for ver in self.adjlist[v]:
                self.adjlist[ver].remove(v)
            self.adjlist.pop(v)
            return True
        return False
                
    
    
            
    def add_edges(self,v1,v2):
        if v1 in self.adjlist.keys() and v2 in self.adjlist.keys():
            self.adjlist[v1].append(v2)
            self.adjlist[v2].append(v1)
            return True
        return False
    
    def remove_edges(self,v1,v2):
        if v1 in self.adjlist.keys() and v2 in self.adjlist.keys():
            try:
                self.adjlist[v1].remove(v2)
                self.adjlist[v2].remove(v1)
            except ValueError :
                pass
            
            return True
        False
        
                   
    def display_graph(self):
        for key,val in self.adjlist.items():
            print(key,val)
            
        print()
            
            

obj = Graph()
obj.add_vertices(4)
obj.add_vertices(8)
obj.add_vertices(12)
obj.add_vertices(36)
obj.display_graph()

obj.add_edges(4,8)
obj.add_edges(4,12)
obj.add_edges(12,36)
obj.add_edges(8,36)
obj.display_graph()

obj.remove_edges(12,4)
obj.add_edges(8,36)
obj.display_graph()

obj.remove_vertics(8)
obj.display_graph()




