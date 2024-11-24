from DS.linked_list import Node, LinkedList

class Solution(object):
    
    def reverseList(self, head: Node) -> Node:
        cur=head
        prev=None
        if not head or not head.next:
            return head
        while(cur):
            front=cur.next
            cur.next=prev
            prev=cur
            cur=front
        return prev

    def reverseList_recursion(self, head:Node) -> Node:
        if not head or not head.next:
            return head
        new_head=self.reverseList2(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head
    
if __name__ == '__main__':
    ll=LinkedList()
    arr=[1,2,3,4,5]
    head=ll.list2ll(arr)