class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        isnil: check whether the index exists
        """
        self.isnil = True
        self.val = None
        self.next = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.isnil:
            return -1
        elif index == 0:
            return self.val
        else:
            return self.next.get(index-1)
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.isnil:
            self.val = val
            self.next = MyLinkedList()
            self.isnil = False
        else:
            new = MyLinkedList()
            new.isnil = False
            new.val = self.val
            new.next = self.next
            self.val = val
            self.new = new
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.isnil:
            self.addAtHead(val)
        else:
            self.next.addAtTail(val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        pass
        # if self.isnil  and index > 0:
        #     return
        # elif index == 0:
        #     if self.isnil:
        #         self.next = None
        #         self.isnil = True
        #     else:
        #         self.next.val = self.val
        #         self.next.next = self.next
        # else:
        #     self.next.addAtIndex(index-1, val)
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.isnil:
            return
        elif index == 0:
            if self.next.isnil:
                self.next = None
                self.isnil = True
            else:
                self.val = self.next.val
                self.next = self.next.next
        else:
            self.next.deleteAtIndex(index - 1)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

linkedList = MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(2);
linkedList.addAtTail(3);
linkedList.deleteAtIndex(1);  ##linked list becomes 1->2->3
print(linkedList.get(1))

linkedList.get(1);            ## returns 2
linkedList.deleteAtIndex(1);  ## now the linked list is 1->3
linkedList.get(1);            ## returns 3