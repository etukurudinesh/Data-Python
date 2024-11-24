from DS.linked_list import Node, LinkedList

class Solution(object):
    
    def add_numbers(self, head1: Node, head2: Node) -> Node:
        if not head1 and not head2:
            return None
        t1=head1
        t2=head2
        cur=dummy=Node(-1, None)
        carry=0
        while t1 is not None or t2 is not None:
            data = carry
            if t1 is not None and t2 is not None:
                data += t1.data + t2.data
                t1=t1.next
                t2=t2.next
            elif t2 is None:
                data += t1.data
                t1=t1.next
            else:
                data += t2.data
                t2=t2.next
            
            cur.next=Node(data%10, None)
            carry = data // 10
            cur=cur.next
        if carry:
            cur.next=Node(carry, None)
        return dummy.next
    
    def add_numbers_optimal(self, l1: Node, l2: Node) -> Node:
        t1=l1
        t2=l2
        dummy_head=Node(-1)
        cur=dummy_head
        carry=0
        while t1 is not None or t2 is not None:
            data=carry
            if t1 is not None and t2 is not None:
                data+=t1.data+t2.data
                t1.data=data%10
                cur.next=t1
                t1=t1.next
                t2=t2.next
            elif t1 is not None:
                data+=t1.data
                t1.data=data%10
                cur.next=t1
                t1=t1.next
            else:
                data+=t2.data
                t2.data=data%10
                cur.next=t2
                t2=t2.next

            cur=cur.next
            carry = data//10
        if carry:
            cur.next=Node(carry)
        return dummy_head.next


if __name__ == '__main__':

    node3=Node(3, None)
    node2=Node(3, node3)
    head=Node(1, node2)

    _node4=Node(9, None)
    _node3=Node(9, _node4)
    _node2=Node(3, _node3)
    _head=Node(1, _node2)

    head2=Solution().add_numbers(head, _head)
    LinkedList().traverse(head2)

    head3=Solution().add_numbers_optimal(head, _head)
    LinkedList().traverse(head3)