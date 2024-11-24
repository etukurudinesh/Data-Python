from DS.linked_list import Node, LinkedList

class Solution(object):
    def bruteforce(self, head: Node, n: int) -> Node:
        cur=head
        c=1
        while cur.next is not None:
            c+=1
            cur=cur.next
        if c==n:
            head=head.next
            return head
        ind=c-n
        cur=head
        c=1
        while c != ind:
            c+=1
            cur=cur.next
        cur.next=cur.next.next
        return head

    def delete_n_from_last(self, head: Node, n: int) -> Node:
        slow=head
        fast=head
        c=n
        while fast.next is not None:
            if c != 0:
                c-=1
                fast=fast.next
            else:
                fast=fast.next
                slow=slow.next
        if c != 0:
            head=head.next
            return head
        front=slow.next
        slow.next=slow.next.next
        front.next=None
        return head
if __name__ == '__main__':
    ll=LinkedList()
    node6=Node(6, None)
    node5=Node(5, node6)
    node4=Node(4, node5)
    node3=Node(3, node4)
    node2=Node(2, node3)
    head=Node(1, node2)
    
    new_head=Solution().bruteforce(head, )
    ll.traverse(new_head)