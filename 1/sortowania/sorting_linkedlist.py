'''sortowanie linked list'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print("None")

#insertion
def insertion(head):
    dummy = Node(0, head)
    prev, current = head, head.next
    while current:
        if current.val >= prev.val:
            prev, current = current, current.next
        tmp = head
        while current.val > tmp.next.val:
            tmp = tmp.next
        prev = prev.next
        current = current.next
        tmp.next = current
        current = prev.next
    return head

#selection
def selection(head):
    pass

#mergesort
def split(head):
    res = head
    while head.next and head.next.next:
        head = head.next.next
        res = res.next
    return res

def mergesort(head):
    if head == None or head.next == None:
        return head

    left_end = split(head)
    middle = left_end.next
    left_end.next = None
    left = mergesort(head)
    right = mergesort(middle)

    return merge(left, right)

def merge(p, q):
    pass