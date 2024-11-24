from DS.linked_list import Node, LinkedList

class Solution(object):

    def swap(self, a, b):
        a=a+b
        b=a-b
        a=a-b

    def sort_(self, arr: list) -> list:
        for i in range(len(arr)-1):
            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    arr[i]=arr[i]+arr[j]
                    arr[j]=arr[i]-arr[j]
                    arr[i]=arr[i]-arr[j]
        return arr

    def merge_sorted_ll(self, list1: Node, list2: Node) -> Node:
        arr=[]
        cur=list1
        while cur.next is not None:
            arr.append(cur.data)
            cur=cur.next
        arr.append(cur.data)
        cur.next=list2
        cur=list2
        while cur is not None:
            arr.append(cur.data)
            cur=cur.next
        cur=list1
        sorted_arr=self.sort_(arr)
        while cur is not None:
            cur.data=sorted_arr.pop(0)
            cur=cur.next
        return list1
    

    def optimized(self, list1: Node, list2: Node):
        if not list1 and not list2:
            return None
        dummy_head=Node(-1, None)
        cur=dummy_head
        x1=list1
        x2=list2
        while x1 is not None and x2 is not None:
            if x2.data > x1.data:
                cur.next=x1
                x1=x1.next
            else:
                cur.next=x2
                x2=x2.next
            cur=cur.next
        if x1 is None:
            cur.next=x2
        else:
            cur.next=x1
        return dummy_head.next

if __name__ == '__main__':
    arr=[13, 1, 4, 12, 9, 27, 21, 23, 14]
    #print(*arr)
    arr2=Solution().sort_(arr)


    ll=LinkedList()
    node7=Node(38, None)
    node6=Node(33, node7)
    node5=Node(29, node6)
    node4=Node(4, node5)
    node3=Node(3, node4)
    node2=Node(3, node3)
    head=Node(1, node2)



    ll=LinkedList()
    _node6=Node(234, None)
    _node5=Node(37, _node6)
    _node4=Node(34, _node5)
    _node3=Node(24, _node4)
    _node2=Node(3, _node3)
    _head=Node(1, _node2)

    head=Solution().optimized(None, Node(3, None))
    ll.traverse(head)
    