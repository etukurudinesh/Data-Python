from DS.linked_list import Node, LinkedList

class Solution(object):

    def length_of_loop(self, head: Node) -> Node:
        cur=head
        hash_t={}
        count=1
        while cur:
            if cur in hash_t:
                return count-hash_t[cur]
            hash_t.update({
                cur : count,
            })
            count+=1
            cur=cur.next
        return 0
    
    def length_of_loop_floyds(seld, head:Node) -> Node:
        slow=fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                slow=head
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                count=1
                slow=slow.next
                while slow != fast:
                    slow=slow.next
                    count+=1
                return count
        return 0
    
    def length_of_loop_floyds_2(seld, head:Node) -> Node:
        slow=fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                counter=1
                slow=slow.next
                while slow != fast:
                    slow=slow.next
                    counter+=1
                return counter
        return 0
    

if __name__ == '__main__':
    ll=LinkedList()
    # create a cycle list
    node5=Node(5, None)
    node4=Node(4, node5)
    node3=Node(3, node4)
    node2=Node(2, node3)
    head=Node(1, node2)
    node5.next = node3


    test=Node(1, None)
    test.next = test

    length=Solution().length_of_loop_floyds_2(head)
    print(length)