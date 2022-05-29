# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:32:58 2022

@author: kundan
"""

class node:
    def __init__(self,value):
        self.value = value
        self.next=None
        
        
class queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=1
        
    
    def enque(self,value):
        new_node = node(value)
        if self.head == None:
            self.head=new_node
            
        else:
            temp=self.tail
            new_node.next=temp.next
            temp.next=new_node
        self.tail = new_node
        self.length += 1
        return True
        
    
    def deque(self):
        temp=self.head
        if temp == None:
            return False
        self.head = temp.next
        self.length -= 1
        return True
        
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
        print()
        
    
obj = queue()
obj.enque(12)
obj.enque(22)
obj.enque(32)
obj.enque(42)
obj.enque(52)
obj.display()

obj.deque()
obj.display()

obj.deque()
obj.display()