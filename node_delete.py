class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list(x):
    head = ListNode(x[0])
    current = head
    for value in x[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


L_list = linked_list([4, 5, 1, 9])
x = L_list.next  
deleteNode(x)
print_list(L_list)

L_list = linked_list([4, 5, 1, 9])
x = L_list 
deleteNode(x)
print_list(L_list)
