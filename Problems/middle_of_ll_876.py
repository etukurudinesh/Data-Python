from DS.linked_list import Node, LinkedList

class Solution(object):
    
    def middleNode(self, head: Node) -> Node:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mid=None
        pos=1
        cur=head
        while(cur.next):
            cur=cur.next
            pos+=1
        mid=(pos//2)+1
        pos=1
        cur=head
        while(cur):
            if pos==mid:
                return cur
            cur=cur.next
            pos+=1
    
    def middleNode2(self, head) -> Node:
        cur=head
        mid=head
        while cur and cur.next:
            mid=mid.next
            cur=cur.next.next
        return mid
            
    
if __name__ == '__main__':
    arr=[1,2,3,4]
    ll=LinkedList()
    head=ll.list2ll(arr)
    head=Solution().middleNode2(head)
    ll.traverse(head)