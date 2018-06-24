class Node:
    '''
    Class to represent nodes in a tree.

    A `Node` has value and a right and a left child which are either
    `Node`s themselves, or `None`

    Args:
        value (int):   value of the node
        left (Node):  [optional] instance of another Node
        right (Node): [optional] instance of another Node

    '''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __cmp__(self, other):
        ''' Compare nodes by their value attribute '''
        if self.value < other.value:
            return -1
        if self.value > other.value:
            return 1
        else:
            return 0


class BST:
    '''
    A BST has a `root` which is either `None` or an instance
    of a `Node` where the left child of the node is less than
    that of the root, and the value of the right child of the
    node is greater. The children can themselves be considered
    binary search trees.

    '''
    def __init__(self, root=None):
        self.root = root

    def _add(self, child, parent):
        if child < parent:
            if parent.left is not None:
                self._add(child, parent.left)
            else:
                parent.left = child
        if child > parent:
            if parent.right is not None:
                self._add(child, parent.right)
            else:
                parent.right = child
        else:
            # child.value == parent.value, do nothing
            pass

    def add(self, node):
        '''
        `node` can either be a `Node` instance, or an `int` which will be
        made into a `Node`
        '''
        if isinstance(node, int):
            node = Node(node)
        if self.root is None:
            self.root = node
        else:
            self._add(node, self.root)

    def _get_min_node(self, root):
        '''
        Return node with minimum value by recursively looking in the
        left subtree
        Assumes `root` is not `None`
        '''
        if root.left is None:
            return root
        else:
            return self._get_min_node(root.left)

    def _remove(self, value, root):
        '''
        Remove `value` from the subtree whose root is `root`
        Returns the root of the new subtree
        '''
        if root is None:
            pass
        elif value < root.value:
            root.left = self._remove(value, root.left)
        elif value > root.value:
            root.right = self._remove(value, root.right)
        else:
            # we need to remove the root
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                # root has 2 children
                # replace root with the next in-order node, which
                # is the smallest in the right subtree
                inordersuccessor = self._get_min_node(root.right)
                # update the value of root, essentially copying the
                # inorder successor to the roots position
                root.value = inordersuccessor.value
                # delete the inordersuccessor from the right subtree
                root.right = self._remove(inordersuccessor.value, root.right)
        # always return the (possibly updated) root
        return root

    def remove(self, value):
        '''
        Remove this value from the tree, if possible
        Returns the new root of the tree
        '''
        return self._remove(value, self.root)

    def _print_tree(self, node, method):
        '''
        Print the tree in the other given by `method`
        '''
        if node is not None:
            if method == "in":
                self._print_tree(node.left, method)
                print node
                self._print_tree(node.right, method)
            elif method == "pre":
                print node
                self._print_tree(node.left, method)
                self._print_tree(node.right, method)
            elif method == "post":
                self._print_tree(node.left, method)
                self._print_tree(node.right, method)
                print node

    def print_tree(self, method="in"):
        '''
        Print the tree. `method` can be one of:
            "in"  : print left substree, root, right subtree
            "pre" : print root, left subtree, right subtree
            "post": print left subtree, right subtree, root
        Default is "in" order

        '''
        if self.root is not None:
            self._print_tree(self.root, method)


def main():
    values = [9, 1, 5, 6, 12, 25, 32, 4, 8]
    bst = BST()
    for value in values:
        bst.add(value)
    #bst.remove(6)
    bst.remove(9)
    bst.print_tree()


if __name__ == '__main__':
    main()
