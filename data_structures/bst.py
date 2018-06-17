'''
Class definition for a binary search tree. This implementation will also
implement the `Node` class for use in the creation of `BST`

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class BST:
    '''
    In this implementation, a BST is either None, or it is a Node with
    two children that are each BSTs. All values of Nodes in the left subtree
    are less than the current Node's value, and all values of Nodes in the
    right subtree are greater than the current Node's value.
    '''
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        ''' node will not be None here so we can update it '''
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        elif val > node.val:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
        else:
            # value is already in tree
            return None

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print node.val
            self._print_tree(node.right)


def main():
    bst = BST()
    bst.add(10)
    bst.add(6)
    bst.add(4)
    bst.add(8)
    bst.add(12)
    bst.add(7)
    bst.print_tree()


if __name__ == '__main__':
    main()
