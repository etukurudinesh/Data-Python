from DS.linked_list import Node, LinkedList

class Solution(object):
    def segregate(self, head: Node) -> Node:
        if head.next is not None:
            return head
        
        odd_head=odd=head
        even_head=even=head.next
        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            
            even.next=even.next.next
            even=even.next
        
        odd.next = even_head
        return odd_head
    
    def bruteforce(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head
        cur=head
        arr=[]
        while cur is not None and cur.next is not None:
            arr.append(cur.data)
            cur=cur.next.next
        if cur is not None:
            arr.append(cur.data)
        cur=head.next
        while cur is not None and cur.next is not None:
            arr.append(cur.data)
            cur=cur.next.next
        if cur is not None:
            arr.append(cur.data)
        cur=head
        while cur is not None:
            cur.data=arr.pop(0)
            cur=cur.next
        return head
if __name__ == '__main__':
    ll=LinkedList()
    
    node6=Node(6, None)
    node5=Node(5, node6)
    node4=Node(4, node5)
    node3=Node(3, node4)
    node2=Node(2, node3)
    head=Node(1, node2)
    new_head=Solution().bruteforce(head)
    ll.traverse(new_head)