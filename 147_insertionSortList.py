# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
def insertionSortList(self, head: 'ListNode') -> 'ListNode':
    ## we need three pointer here, p is the position where cur is gonna inser after
    ## cur is the element we need to compare each time
    ## dummy is to return the sorted list, and in case head is changed
    p = dummy = ListNode(0)
    cur = dummy.next = head

    ## traverse to the last second node 
    while cur and cur.next:
        ## compare cur ndoe with next node val
        ## if the sequence is sorted already, keep looking ahead
        ## continue is a must here for the next iteration
        next_val = cur.next.val
        if cur.val <= next_val:
            cur = cur.next 
            continue

        ## if there is an element which is smaller than previous sequence
        ## we need to find a proper postion to insert this small element
        if p.next.val > next_val:
            p = dummy

        ## p stops at the element which is smaller than next_val
        ## eg 1,2,5,6,7,4, 8,9 --> since 4 is bigger than 1, 2
        ## we use p.next.val to compare, hence p would point element 2
        ## update: cur would point at 7
        while p.next.val <= next_val:
            p = p.next 

        ## exchange, insertion
        ## for the above example, p.next should be cur.next which is 4
        ## cur.next.next should concatenate the elements in the sorted sequence, in this case 5,6,7
        ## cur.next should be cur.next.next which is 8
        ## update: basically it's an operation to find the proper position of the cur.next.val and reconstruct the list
        ## update2: if we break the syntax down, it becomes:
        ## new = cur.next
        ## cur.next = new.next
        ## new.next = p.next
        ## p.next = new
        
        p.next, cur.next.next, cur.next =cur.next, p.next, cur.next.next

    return dummy.next 

