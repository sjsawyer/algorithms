'''
Given a binary tree, count the total number of subtrees of the tree that are
unival tree, where we define a unival tree as being a perfect binary tree whose
values are all the same, and a subtree as being all nodes between heights h1
and h2 of the tree.

So for the following trees,

tree1:       4         tree2:   4
           /   \              /   \
          4     4            4     4
         / \   / \          / \   / \
        4   4 4   4        4   4 4   0

in tree1, each node is its own unival tree, followed by three subtrees of depth
2, followed by the entire tree of depth 3, giving 11 total unival subtrees.

In tree2, each node is its own unival tree, followed by the 2 subtrees of depth
2 consisting of all 4's.

NOTE: This question uses a different definition of what consistutdes a unival
tree than is seen in a similar popular question on the internet.

'''

class Node():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_universal_subtrees(root):
  '''
  Count the total number of universal subtrees from `root` and below
  '''
  n_unival_trees_using_root = dict()  # maps node instances to numbers

  def _count_universal_subtrees(root):
    '''
    Utility function which has access to the `n_unival_trees_using_root` map.
    '''
    # Base case
    if root is None:
      n_unival_trees_using_root[root] = 0
      return 0

    total = 0
    # count number of universal subtrees
    total += _count_universal_subtrees(root.left)
    total += _count_universal_subtrees(root.right)

    # now check to see how many unival trees we are a part of
    n_unival_trees_using_root[root] = 1
    if root.left is not None and root.right is not None:
      if root.left.val == root.right.val == root.val:
        # by the time we get here, values for the children of root should
        # have already been populated in the dictionary
        n_left = n_unival_trees_using_root[root.left]
        n_right = n_unival_trees_using_root[root.right]
        n_unival_trees_using_root[root] += min(n_left, n_right)

    total += n_unival_trees_using_root[root]

    return total

  return _count_universal_subtrees(root)


def main():
    # Test the trees illustrated above
    tree1 = Node(4)
    tree1.left = Node(4); tree1.right = Node(4)
    tree1.left.left = Node(4); tree1.left.right = Node(4)
    tree1.right.left = Node(4); tree1.right.right = Node(4)

    tree2 = Node(4)
    tree2.left = Node(4); tree2.right = Node(4)
    tree2.left.left = Node(4); tree2.left.right = Node(4)
    tree2.right.left = Node(4); tree2.right.right = Node(0)

    assert count_universal_subtrees(tree1) == 11
    assert count_universal_subtrees(tree2) == 9


if __name__ == '__main__':
    main()
