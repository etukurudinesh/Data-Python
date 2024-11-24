from __future__ import annotations
class Node:
    # instance variables
    def __init__(self, data: int=None, next: Node=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(id(self))

class LinkedList:
     
    def __init__(self):
        self.head = None
        self.tail = None

    def list2ll(self, arr: list) -> Node:
        """
        Summary: Converts list into linked list
        Input: list
        Return value: Node
        """
        if not arr:
            return None
        # keep track of head - the cur pointer in the linked list
        self.head = cur = Node(arr[0])
        
        # moving an entire array into linked list
        for data in arr[1:]:
            temp: Node = Node(data, None)
            # head node is the current pointer in the linked list
            cur.next = temp
            cur = temp
        return self.head
     
    def len_ll(self, head: Node) -> int:
        """
        Summary: Returns the length of the linked list
        Input: Node (head)
        Return value: int
        """
        counter = 0
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next
            counter+=1
        return counter
    
    def traverse(self, head: Node) -> None:
        """
        Summary: Traverses and prints all the elements in the linked list
        Input: head node
        Return: None
        """
        data_width = 8
        address_width = 15

        temp = head
        print(f'{"Data":<{data_width}} | {"Memory Address":<{address_width}}')
        print(f"{'-':-^31}")
        while(temp):
            print(f'{temp.data:<{data_width}} | {id(temp):<{address_width}}')
            temp = temp.next

    def check_element(self, head: Node, element: int) -> bool:
        """
        Summary: Checks if the given element is present in the linked list
        Input: head node & element
        Return value: boolean
        """
        temp=head
        while temp:
            if temp.data==element:
                return True
            temp=temp.next
        return False
    
    def insert_head(self, head: Node, value: int) -> Node:
        """
        Summary:
        Input:
        Return Value:
        Time-complexity: O(1)
        """
        if not head:
            return Node(value, None)
        temp = Node(value, head)
        return temp

    def insert_end(self, head: Node, element: int) -> Node:
        """
        
        """
        temp=Node(element, None)
        if not head:
            return temp
        cur=head
        while cur.next:
            cur=cur.next
        cur.next=temp
        return head

    def insert_before_element(self, head: Node, element: int, value: int) -> Node:
        """
        Summary:
        Input:
        Return value:
        """
        if not head:
            return Node(value, None)
        if element==head.data:
            return self.insert_head(head, value)
        cur=head
        prev=None
        while(cur):
            #[10, 20, 30]
            if cur.next.data==element:
                temp=Node(value, None)
                temp.next = cur.next 
                cur.next = temp
                break
            cur=cur.next
        return head
    
    def insert_index(self, head: Node, index: int, value: int) -> Node:
        """
        Summary:
        Input:
        Return value:
        """
        # if index is 1 then insert in head
        if index == 1:
            return self.insert_head(head, value)
        # if there is no linked list return none
        if not head:
            return None
        cur=head
        pos=1
        while(cur):
            if pos == index-1:
                temp=Node(value, None)
                temp.next = cur.next 
                cur.next = temp
                break
            cur=cur.next
            pos+=1
        return head

    def delete_head(self, head: Node) -> Node:
        if not head or not head.next:
            return None
        head = head.next
        return head
        
    def delete_end(self, head: Node) -> Node:
        if not head or not head.next:
            return None
        cur=head
        while cur.next.next:
            cur=cur.next
        cur.next = None
        return head

    def delete_index(self, head: Node, k: int) -> Node:
        """
        Summary: deletes the node at the kth element
        Input: head node and kth element
        Return value: node
        """
        # edge case-1: if the position is the head or start
        if k==1:
            return self.delete_head(head)
        # if the postion is out of bound then return head
        if k<=0:
            return head
        # if the linked list is empty
        if not head:
            return None
        cur=head
        # keeps a track of the previous node
        prev=None
        # track the current element location
        c=1
        # keeps bounday check
        while cur:
            # if we reach the desired element update the previous node
            if c==k:
                prev.next=prev.next.next
                break
            # keep track of previous for each traversal
            prev = cur
            cur=cur.next
            c+=1
        return head
    
    def delete_value(self, head: Node, element: int ) -> Node:
        # if head is null return None 
        if not head:
            return None
        # if head is the element remove head
        if head.data==element:
            self.delete_head(head)
        # if element is in the middle
        cur=head
        prev=None
        while cur:
            if cur.data==element:
                # handles the logic for removing tail
                prev.next=prev.next.next
                break
            prev=cur
            cur=cur.next

    def traverse_recursion(self, head: Node) -> Node:
        if not head:
            return
        self.traverse_recursion(head.next)
        print(head.data)

    def find_ll_recursion(self, head: Node, element: int) -> bool:
        if not head:
            return False
        if head.data==element:
            return True
        return self.search_ll_recursion(head.next, element)

if __name__ == '__main__':
    
    arr: int=[5, 6, 7, 9, 14, 20, 28]
    arr2:int = [] 
    ll: LinkedList=LinkedList()
    head: Node=ll.list2ll(arr)
    head: Node=ll.insert_index(head, index=2, value=20)
    head: Node=ll.insert_before_element(head, element=9, value=24)
    ll.traverse(head) 