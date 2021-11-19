from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    if head is None or head.next is None:
        return head

    curr = head
    prev = None
    i = 0
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    first_part_last_node = prev
    sub_list_last_node = curr

    i = 0
    while curr and i < q - p + 1:
        nextElem = curr.next
        curr.next = prev
        prev = curr
        curr = nextElem
        i += 1

    if first_part_last_node:
        first_part_last_node.next = prev
    else:
        head = prev
    sub_list_last_node.next = curr

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
