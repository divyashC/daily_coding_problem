# Day 3
# Problem 3
# Date 12 Feb 2021
# Time 9:25 AM

"""
Test case
node = Node('node', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


list = []


def deserialize(node_list, root=None):
    if node_list:
        val = node_list.pop(0)
    else:
        return

    # Create root, left and right recursively
    root = Node(val)
    root.left = deserialize(node_list, root.left)
    root.right = deserialize(node_list, root.right)
    return root


def serialize(node):
    if node is None:
        return

    list.append(node.val)
    serialize(node.left)
    serialize(node.right)
    return list


node = Node('node', Node('left', Node('left.left')), Node('right'))
if (deserialize(serialize(node)).left.left.val == 'left.left'):
    print(True)
else:
    print(False)
