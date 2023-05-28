#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:27:49 2023

@author: farid
"""

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]


Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
    def __repr__(self):
        if self.next is None:
            #f"ListNode{{val: {self.val}, next: None}} "
            return f"({self.val}),(None)"
        else:
            #f"ListNode{{val: {self.val}, next: {repr(self.next)}}}"
            return f"({self.val}),({repr(self.next)})"

# Creating list1: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)
# print(list1)



class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        # print(curr, "\n\n")
        while curr is not None:
            next_node = curr.next
            # print("curr.next  ===> ", curr.next, )
            # print("prev   ===> ", prev, )
            curr.next = prev
            print("curr.next  xxxxxx>> ", curr.next )
            prev = curr
            print("prev  //===>  ", prev ,"\n")
            curr = next_node
            # print("next node   ", next_node , "\n curr  ", curr,  )
            # print("\n\n\n\n")
        return prev
    
    
a = Solution().reverseList(list1)
print(a)


#=================Understand output for insight==================
'''
given:
    
  list1 or curr =====>    [ (1),(2),(4),(5),(None) ]
  prev ========>          None
 

four steps to reverse listnode:
    
==> Step1:    --------------------------------
next_node = curr.next     -->  [(2),(4),(5),(None) ]

curr.next = prev          --> None

prev = curr               -->  [(1),(None)]

curr = nextnode           --> [(2),(4),(5),(None) ]

==> Step2:-------------------------------------
next_node = curr.next     -->  [(4),(5),(None) ]

curr.next = prev          --> [(1),(None)]

prev = curr               -->  [(2), (1),(None)]

curr = nextnode           --> [(4),(5),(None) ]
    

==> Step3:    ------------------------------
next_node = curr.next     -->  [(5),(None) ]

curr.next = prev          --> [(2),(1),(None)]

prev = curr               -->  [(4), (2), (1),(None)]

curr = nextnode           --> [(5),(None) ]

==> Step4:   -----------------------------
next_node = curr.next     -->  [(None) ]

curr.next = prev          --> [(4), (2),(1),(None)]

prev = curr               -->  [(5), (4), (2), (1),(None)]

curr = nextnode           --> [(None) ]


return prev
'''