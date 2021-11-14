def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            A, B = headA, headB
        while A!=B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A