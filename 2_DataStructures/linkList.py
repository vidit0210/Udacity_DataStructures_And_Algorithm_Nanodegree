class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(3)
# next_value = Node(4)
# head.next = next_value
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(6)


def print_linked_list():
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


# print_linked_list()


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                # Move to the tail (The last Node)
                current_node = current_node.next
            current_node.next = Node(value)
    return head


ll = create_linked_list([3, 4, 5, 6])


def create_better_linked_list(input_list):
    head = None
    tail = None
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head


llb = create_better_linked_list([1, 7, 8, 9.2])
# print(llb.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)

        # Need to move to the tail to Append the Value
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return
