from DS.linked_list import Node, LinkedList

class Solution(object):
    
    def is_cyclic(self, head: Node) -> bool:
        hash_t={}
        cur=head
        if not head or not head.next:
            return head
        while(cur):
            if cur not in hash_t:
                hash_t.update({
                    cur : 1
                })
            else:
                return True
            cur=cur.next
        return False
    
    def is_cylic_tortoise_hare(self, head: Node) -> bool:
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

if __name__ == '__main__':
    arr: int=[5, 6, 7, 9, 14, 20, 28]

    test=Node(1, None)
    test.next = test

    ans=Solution().is_cylic_tortoise_hare(test)
    print(ans)