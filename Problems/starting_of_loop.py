from DS.linked_list import Node, LinkedList

class Solution(object):
    
    def start_of_loop(self, head: Node) -> Node:
        """ Use Hash table - Sets"""
        set_t=set()
        if not head:
            return head
        cur=head
        while cur:
            if cur in set_t:
                return cur.data
            set_t.add(cur)
            cur=cur.next
        return None
    
    def start_of_cycle_floyds(self, head: Node) -> Node:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                slow=head
                while slow != head:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None

if __name__ == '__main__':
    ll=LinkedList()
    # create a cycle list
    node5=Node(5, None)
    node4=Node(4, node5)
    node3=Node(3, node4)
    node2=Node(2, node3)
    head=Node(1, node2)
    node5.next = head
    loop_start2=Solution().start_of_cycle_floyds(head)
    print(loop_start2.data)