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
    def __init__(self,q_obj):
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
                
    
                
   
    
    def preorder(self,temp):
        if temp is not None:
            print(temp.value)
            self.preorder(temp.left)
            self.preorder(temp.right)
            
            
    def inorder(self,temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.value)
            self.inorder(temp.right)
            
    def postorder(self,temp):
        if temp is not None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.value)
            
            
    def bfs(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return results


             
        
        
        
        
ck = binary_search_tree(q_obj)   
        
ck.insert(60)
ck.insert(100)
ck.insert(50)
ck.insert(40)
ck.insert(10)
ck.insert(80)
ck.insert(120)
        

print('Bfs')
results=ck.bfs()
print(results)
