from DS.linked_list import Node, LinkedList

class Solution(object):

    def palindrome(self, head: Node) -> Node:
        slow=fast=head
        stack=[]
        if not head:
            return False
        while fast is not None and fast.next is not None:
            stack.append(slow.data)
            slow=slow.next
            fast=fast.next.next
        print(stack)
        if fast is not None:
            slow=slow.next
        while slow != None:
            if slow.data != stack.pop():
                return False
            slow=slow.next
        return True
    
    def palindrome_bruteforce(self, head: Node) -> Node:
        stack_=[]
        cur=head
        while cur is not None:
            stack_.append(cur.data)
            cur=cur.next
        cur=head
        while cur is not None:
            if cur.data != stack_.pop():
                return False
            cur=cur.next
        return True

    def reverse(self, head: Node) -> Node:
        prev=None
        cur=head
        while cur:
            front=cur.next
            cur.next=prev
            prev=cur
            cur=front
        return prev
        
    def palindrome_reverse(self, head: Node) -> Node:
        cur=fast=head
        while fast.next is not None and fast.next.next is not None:
            cur=cur.next
            fast=fast.next.next
        new_head=self.reverse(cur.next)
        rev=new_head
        cur=head
        while rev:
            if cur.data != rev.data:
                self.reverse(new_head)
                return False
            cur=cur.next
            rev=rev.next
        self.reverse(new_head)
        return True

if __name__ == '__main__':
    ll=LinkedList()
    # create a cycle list
    node6=Node(1, None)
    node5=Node(2, node6)
    node4=Node(4, node5)
    node3=Node(4, node4)
    node2=Node(2, node3)
    head=Node(1, node2)
    length=Solution().palindrome_reverse(head)
    print(length)