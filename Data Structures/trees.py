"""
A tree is a collection of nodes. Nodes are connected by edges. Each node contains a value or data, and it may or may not
have a child node.
A graph without loops.

A binary tree is a tree data structure in which each node has at the most two children.
A binary search tree is sometimes called ordered or sorted binary trees, and it keeps its values in sorted order,
so that lookup and other operations can use the principle of binary search. A property of a BST is that the value of
BST node is larger that the value of the offspring of its left child, but smaller than the value of offspring of its
right child.
"""
from queue import Queue
from typing import Union, Optional


class BinaryTree:
    def __init__(self, cargo: Union[str, int]):
        self.cargo = cargo
        self.left: Optional[BinaryTree] = None
        self.right: Optional[BinaryTree] = None

    def insert_left(self, cargo: int) -> None:
        if not self.left:
            self.left = BinaryTree(cargo)
        else:
            new_node = BinaryTree(cargo)
            new_node.left, self.left = self.left, new_node

    def insert_right(self, cargo: int) -> None:
        if not self.right:
            self.right = BinaryTree(cargo)
        else:
            new_node = BinaryTree(cargo)
            new_node.right, self.right = self.right, new_node

    def pre_order_traversal(self):
        print(self.cargo)

        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()

        print(self.cargo)

        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.cargo)

    def breadth_first_search(self):
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            current_node: BinaryTree = queue.get()
            print(current_node.cargo)
            if current_node.left:
                queue.put(current_node.left)
            if current_node.right:
                queue.put(current_node.right)


class BinarySearchTree:
    def __init__(self, cargo: Union[int, str]):
        self.cargo = cargo
        self.left: Optional[BinarySearchTree] = None
        self.right: Optional[BinarySearchTree] = None

    def insert_node(self, cargo: Union[int, str]) -> None:
        if cargo <= self.cargo and self.left:
            self.left.insert_node(cargo)
        elif cargo <= self.cargo:
            self.left = BinarySearchTree(cargo)
        elif cargo > self.cargo and self.right:
            self.right.insert_node(cargo)
        else:
            self.right = BinarySearchTree(cargo)

    def find_node(self, target: Union[int, str]) -> bool:
        if target < self.cargo and self.left:
            return self.left.find_node(target)
        if target > self.cargo and self.right:
            return self.right.find_node(target)
        return target == self.cargo

    @property
    def min_element(self):
        if self.left:
            return self.left.min_element
        else:
            return self.cargo


if __name__ == '__main__':
    print('Running all tests...')
    tree = BinaryTree('a')
    print(tree.cargo)
    bst = BinarySearchTree(15)
    bst.insert_node(10)
    bst.insert_node(8)
    bst.insert_node(12)
    bst.insert_node(20)
    bst.insert_node(17)
    bst.insert_node(25)
    bst.insert_node(19)
    assert bst.find_node(15) is True
    assert bst.find_node(10) is True
    assert bst.find_node(8) is True
    assert bst.find_node(0) is False
    assert bst.min_element is 8
