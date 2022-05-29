# -*- coding: utf-8 -*-
"""
Created on Sat May 28 09:39:17 2022

@author: kundan
"""

class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.top=1
        
        
        
class stack:
    
    def __init__(self):
        self.head=None
        self.top = 1
        
        
    def push(self,value):
        new_node = node(value)
        new_node.next = self.head
        self.head=new_node
        self.top += 1
        return value
        
    
    
    def pop(self):
        if self.head is None:
            return False
        temp=self.head
        self.head=temp.next
        self.top -= 1
        return True
    
    
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
        print()
            
            
            

    
    
obj  = stack()
obj.push(30)
obj.push(50)
obj.push(80)
obj.push(60)
obj.push(10)
obj.push(20)

obj.display()

obj.pop()
obj.display()

obj.pop()
obj.display()