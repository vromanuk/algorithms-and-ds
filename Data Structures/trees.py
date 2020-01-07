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
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None

    def insert_left(self, cargo: int) -> None:
        if not self.left_child:
            self.left_child = BinaryTree(cargo)
        else:
            new_node = BinaryTree(cargo)
            new_node.left_child, self.left_child = self.left_child, new_node

    def insert_right(self, cargo: int) -> None:
        if not self.right_child:
            self.right_child = BinaryTree(cargo)
        else:
            new_node = BinaryTree(cargo)
            new_node.right_child, self.right_child = self.right_child, new_node

    def traverse_tree_pre_order(self):
        print(self.cargo)

        if self.left_child:
            self.left_child.traverse_tree_pre_order()
        if self.right_child:
            self.right_child.traverse_tree_pre_order()

    def traverse_tree_in_order(self):
        if self.left_child:
            self.left_child.traverse_tree_in_order()

        print(self.cargo)

        if self.right_child:
            self.right_child.traverse_tree_in_order()

    def traverse_tree_post_order(self):
        if self.left_child:
            self.left_child.traverse_tree_post_order()
        if self.right_child:
            self.right_child.traverse_tree_post_order()
        print(self.cargo)

    def breadth_first_search(self):
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            current_node: BinaryTree = queue.get()
            print(current_node.cargo)
            if current_node.left_child:
                queue.put(current_node.left_child)
            if current_node.right_child:
                queue.put(current_node.right_child)


class BinarySearchTree:
    def __init__(self, cargo: Union[int, str]):
        self.cargo = cargo
        self.left_child: Optional[BinarySearchTree] = None
        self.right_child: Optional[BinarySearchTree] = None

    def insert_node(self, cargo: Union[int, str]) -> None:
        if cargo <= self.cargo and self.left_child:
            self.left_child.insert_node(cargo)
        elif cargo <= self.cargo:
            self.left_child = BinarySearchTree(cargo)
        elif cargo > self.cargo and self.right_child:
            self.right_child.insert_node(cargo)
        else:
            self.right_child = BinarySearchTree(cargo)

    def find_node(self, target: Union[int, str]) -> bool:
        if target < self.cargo and self.left_child:
            return self.left_child.find_node(target)
        if target > self.cargo and self.right_child:
            return self.right_child.find_node(target)
        return target == self.cargo

    @property
    def min_element(self):
        if self.left_child:
            return self.left_child.min_element
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
