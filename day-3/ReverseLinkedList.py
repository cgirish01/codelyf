def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return prev
  
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)