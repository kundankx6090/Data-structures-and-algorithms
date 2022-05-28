# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:12:31 2022

@author: kundan
"""

class bstnode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
        
class binary_search_tree:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        node = bstnode(value)
        if self.root is None:
            self.root=node
            return True
        temp=self.root
        while(True):
            if temp.value == node.value:
                return False
            if temp.value>node.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp=temp.left
                
            elif temp.value<node.value:
                if temp.right is None:
                    temp.right = node
                    return True
                temp=temp.right
                
    
                
            
    def find(self,value):        
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
                
            if value > temp.value:
                temp = temp.right
                
        return False
    
    
    
    def min_val(self):
        min = None
        temp=self.root
        while temp is not None:
            if temp.left is None:
                min = temp.value
                
            temp = temp.left
            
            
        return min
    
    def max_val(self):
        min = None
        temp=self.root
        while temp is not None:
            if temp.right is None:
                min = temp.value
                
            temp = temp.right
            
            
        return min
            
        
        
        
        
        
        
        
ck = binary_search_tree()   
        
ck.insert(60)
ck.insert(50)
ck.insert(40)
ck.insert(10)
ck.insert(80)
        
print(ck.root.value)
print(ck.root.left.value)
print(ck.root.left.left.value)
print(ck.root.left.left.left.value)
print(ck.root.right.value)

        
ck.find(40)

ck.find(140)
        
ck.min_val()
ck.max_val()