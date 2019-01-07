class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        mid=self.getmiddle(head)
        lHead=head
        rHead=mid.next
        mid.next=None
        
        return self.merge(self.sortList(lHead),self.sortList(rHead))
    
    def getmiddle(self,head):
        
        if head is None:
            return head
            
        fast=slow=head
        
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow
        
    
    def merge(self,lHead,rHead):
        dumNode=ListNode(0)
        dumHead=dumNode
        
        i=lHead
        j=rHead
        
        while i and j:
            if i.val<j.val:
                dumNode.next=i
                i=i.next
            else:
                dumNode.next=j
                j=j.next
            dumNode=dumNode.next
        
        if i:
            dumNode.next=i
        if j:
            dumNode.next=j
        
        return dumHead.next