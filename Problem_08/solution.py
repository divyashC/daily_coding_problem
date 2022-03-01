# Day 8
# Problem 8
# Date 17 Feb 2022
# Time 7:55 AM

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def count_trees(root):
    if (not root):
        return 0
    elif (not root.left and not root.right):
        return 1
    elif (not root.left and root.val == root.right.val):
        return 1 + count_trees(root.right)
    elif (not root.right and root.val == root.left.val):
        return 1 + count_trees(root.left)

    childrencount = count_trees(
        root.left) + count_trees(root.right)
    curr_count = 0
    if (root.val == root.left.val and root.val == root.left.val):
        curr_count = 1

    return (curr_count + childrencount)


node1 = Node('0')
node2 = Node('1')
node3 = Node('0')
node4 = Node('1')
node5 = Node('0')
node6 = Node('1')
node7 = Node('1')

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
node4.left = node6
node4.right = node7

print(count_trees(None) == 0)
print(count_trees(node1) == 5)
print(count_trees(node3) == 4)
print(count_trees(node7) == 1)
print(count_trees(node4) == 3)
