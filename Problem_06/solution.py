# Day 6
# Problem 6
# Date 15 Feb 2022
# Time 5:45 PM

# implement XOR linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.both = id(value)

    def __repr__(self):
        return str(self.value)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

id_map = dict()
id_map[id("a")] = a
id_map[id("b")] = b
id_map[id("c")] = c
id_map[id("d")] = d
id_map[id("e")] = e


class LinkedList:

    def __init__(self, node):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

    def add(self, element):
        self.tail.both ^= id(element.value)
        element.both = id(self.tail.value)
        self.tail = element

    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.value)
            result_node = id_map[next_node_address]
        return result_node.value


linkedList = LinkedList(c)
linkedList.add(d)
linkedList.add(e)
linkedList.add(a)

print(linkedList.get(0) == "c")
print(linkedList.get(1) == "d")
print(linkedList.get(2) == "e")
print(linkedList.get(3) == "a")
