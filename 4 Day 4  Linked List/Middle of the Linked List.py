#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 00:40:43 2023

@author: farid
"""

'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
    def __repr__(self):
        if self.next is None:
            #
            return f"ListNode{{val: {self.val}, next: None}} "
        else:
            #
            return f"ListNode{{val: {self.val}, next: {repr(self.next)}}}"

# Creating list1: 1 -> 2 -> 4 ->5 -> 5
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)
list1.next.next.next.next = ListNode(5)
# print(list1)

#======================== first solution =======================

class Solution(object):
    def Middle_of_the_linked_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        count = []
        while curr is not None:
            next_node = curr.next
            curr = next_node
            count.append(1)
        indx=""
        total = int(len(count)%2)
        if total ==0:
            indx = int(len(count)/2)+1
        else:
            indx = int(len(count)/2)+1
        x =1
        while head is not None:
            next_node = head.next 
            if x >= indx:
                prev = head
                break
            x+=1
            head = next_node 
            
            
       
        return prev
    
    
a = Solution().Middle_of_the_linked_list(list1)
print(a)

#====================  Second Solution ============================
class Solution(object):
    def Middle_of_the_linked_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
    
        slowPtr = fastPtr = head
    
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if fastPtr is not None:
                slowPtr = slowPtr.next
                break
        return slowPtr
    
a = Solution().Middle_of_the_linked_list(list1)
print(a)
