class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_at(self, pos, data):
        new_node = Node(data)
        if pos < 1:
            raise IndexError("Position must be >= 1")
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(pos - 2):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node

    def delete_nth(self, pos):
        if self.head is None:
            raise Exception("Cannot delete from an empty list")
        if pos < 1:
            raise IndexError("Position must be >= 1")
        if pos == 1:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(pos - 2):
            if current is None or current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        if current.next is None:
            raise IndexError("Position out of range")
        current.next = current.next.next
