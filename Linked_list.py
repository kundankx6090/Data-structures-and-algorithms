# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:59:15 2022

@author: kundan
"""

class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
        
        

class linked_list:
    def __init__(self,value):
        new_node = node(value) 
        self.head=new_node
        self.tail=new_node
        self.length=1
        
        
    def push_beg(self,value):
        node1 = node(value)
        node1.next=self.head
        self.head=node1
        self.length +=1
        return value
            
        
    def push_end(self,value):
        new_node=node(value)
        temp = self.tail
        temp.next=new_node
        self.tail=new_node
        self.length += 1
        return value

        
    def push(self,value,pos):
        if pos<0 or pos>self.length:
            return False
        elif pos==0:
            return self.pop_beg(value)
        
        elif pos==self.length:
            return self.pop_beg
        
        else:
            new_node=node(value)
            temp = self.head
            for _ in range(0,pos-1):
                temp=temp.next
            post=temp.next
            temp.next=new_node
            new_node.next=post
            self.length += 1
            return value
        
    def pop_beg(self):
        temp=self.head
        self.head = temp.next
        self.length -= 1
        
    
    def pop_end(self):
        temp = self.head
        len=self.length
        for i in range(0,len-2):
            temp=temp.next
        self.tail=temp
        temp.next=None
        self.length -= 1
        return temp.value
        
    
    def pop(self,pos):
        if pos==0 or pos>self.length:
            return False
        elif pos == 1:
            self.pop_beg()
            return True
                
        elif pos == self.length-1:
            self.pop_end
            return True
                
        else:
            temp=self.head
            for _ in range(0,pos-2):
                temp=temp.next
                post=temp.next
                temp.next=post.next
            self.length -= 1
            return temp.value
        
        
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
            
        
            
            
    def display(self):
        temp = self.head
        print("Elements in the linked list are : ")
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
        print()
    
        
    
    
        
    
