# MERGE TWO SORTED LIST
## QUESTION:
You are given the heads of two sorted linked lists `list1` and `list2`.  
`Merge` the two lists into one sorted list. The list should be made by `splicing` together the nodes of the first two lists.  
Return the `head` of the merged linked list.  

`Example 1`:  
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]  

`Example 2`:  
Input: list1 = [], list2 = []  
Output: []  

`Example 3`:  
Input: list1 = [], list2 = [0]  
Output: [0]  

## My Solutions:
This is the problem related to the `linked list`. The main idea behind the solution is to create a `dummy node` and `compare` the values between the `lists` and then add it to the `next` node and by that process we append the values from both the lists and `merge` them.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            
            elif list2.val <= list1.val:
                current.next = list2
                current = list2
                list2 = list2.next

        current.next = list1 if list1 else list2     #check the condition for the lists being empty and attach whichever list is not empty

        return dummy.next
```
