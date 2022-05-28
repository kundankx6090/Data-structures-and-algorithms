# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:44:51 2022

@author: kundan
"""
# This class contains basic sorting algorithms
class sort:
    
    
    def swap(self,val1,val2):
        temp=val1
        val1=val2
        val2=temp
        
        return val1,val2
        
        
    def bubble_sort(self,lst):
        for i in range(len(lst)-1,0,-1):
            for j in range(i):
                if lst[j]>lst[j+1]:
                    lst[j],lst[j+1]=self.swap(lst[j],lst[j+1])
                    
        return lst
            
        
    
    def insertion_sort(self,lst):
        for i in range(1,len(lst)):
            for j in range(i,0,-1):
                if lst[j]<lst[j]:
                    lst[i],lst[j]=self.swap(lst[i],lst[j])
                    break
                  
        return lst       
    
    def selection_sort(self,lst):
        for i in range(len(lst)-1):
            min=i
            for j in range(i+1,len(lst)):
                
                if lst[min]>lst[j]:
                    min=j
            
            if i != min:
                lst[i],lst[min] = lst[min],lst[i]
            
        return lst
        
        
    
    def merge(self,left,right):
        i=0
        j=0
        combined=[]
        while i<len(left)  and j<len(right):
            if left[i]<right[j]:
                combined.append(left[i])
                i += 1                
                
            else:
                combined.append(right[j])
                j += 1
            
        while i<len(left):
            combined.append(left[i])
            i += 1
            
            
        while j<len(right):
            combined.append(right[j])
            j += 1
            
            
        return combined
            
            
                
    
    def merge_sort(self,ls):
        
        if len(ls) == 1:
            return ls
        
        mid = int(len(ls)/2)
        left=ls[:mid]
        right=ls[mid:]
        
        return self.merge(self.merge_sort(left),self.merge_sort(right))
            
    
    def pivot(self,ls,left,right):
        
        pivot_index=left
        index=left
        for i in range(left+1,right):
            if ls[i]<ls[pivot_index]:
                index += 1
                st[i],lst[index]=self.swap(lst[i],lst[index])

                
        _,ls[index] = ls[index],ls[pivot_index]
        pivot_index = index
        
        return pivot_index
                
    def quick_sort(self,lst):
        return self.quick_sort_2(lst,0,len(lst)-1)
    
    def quick_sort_2(self,lst,left,right):
        
        if left<right:
            
            pivot_index = self.pivot(lst,left,right)
            
            self.quick_sort_2(lst,left,pivot_index-1)
            self.quick_sort_2(lst,pivot_index+1,right)
            
        return lst

    

lst = [5,9,14,2,7,30,11]
ob = sort()

l1=ob.bubble_sort(lst)
l2=ob.insertion_sort(lst)
print(l1)
print(l2)

l3 = ob.merge_sort(lst)
print(l3)

l4 = ob.quick_sort(lst)
print(l4)

l5 = ob.selection_sort(lst)
print(l5)
