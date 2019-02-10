'''
Q: Given a binary tree with nodes whose values are integers, and an integer
   `s`, find the number of all contiguous paths in the tree whose elements sum
   to `s` (the path needs not start at the root node or end at a leaf node).

   E.g. For the following tree and sum `s=8`,

                10
               /  \
             -2    4
             /    / \
            1    3   4
                /   /
              -2   5

   the contiguous paths that sum to 8 are

     [10, -2]
     [4, 4]

   so we would return 2.


A: To accomplish this, we can use the same technique that we used in
   'logic/contiguous_array_sum.py', where for a given array we stored the
   accumulative sums of the array in a hash table and at any given
   index i, checked to see if the difference between the accumulative sum
   up to index i and our target sum existed in the hash table.

   We can do the same thing here, except we keep track of the accumulative
   sums along the current path in the tree. When we reach the end of a path,
   we backtrack, updating our sums in the hash table.

   For a tree with N nodes and height h, the runtime is O(N) and the space
   complexity is O(h).

'''


class Node():
    '''
    Data structure for a node, which has a `value`, a `left` child and a
    `right` child which are either `Node`s themselves, or `None`.
    '''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def contiguous_subpath_in_tree_sum(t, s):
    '''
    Determine the number of all contiguous subpaths in the tree `t` whose
    values sum to `s`
    '''
    def _contiguous_subpath_in_tree_sum_sofar(end_node, sum_table, sum_so_far):
        '''
        Determine the number of contiguous subpaths that reach from the root
        node to `end_node` and onwards, where the path must end at `end_node`
        or any node which is a descendant of `end_node`, and is not necessarily
        inclusive of the root node of `t`.

        Args:
            end_node: `Node` instance, or None
            sum_table: `dict` which contains the number of subpaths from the
                root node of `t` to `end_node` (exclusive of `end_node`)
            sum_so_far: `int`, the current sum from the root node of `t` to
                `end_node` (exclusive of `end_node`)

        Returns: `int`, the total number of contiguous subpaths from root node
            of `t` to `end_node` (inclusive), or any of `end_node`'s
            descendants, that sum to `s`

        '''
        paths_from_here = 0
        if end_node is None:
            return paths_from_here
        # update sum so far
        sum_so_far += end_node.value
        # check if all nodes from root to end_node sum to s
        if sum_so_far == s:
            paths_from_here += 1
        # check if the difference from here and `s` is in the table, as
        # these constitute desired subpaths
        if (sum_so_far - s) in sum_table:
            paths_from_here += sum_table[sum_so_far - s]
        # Add ourselves to the table
        sum_table[sum_so_far] = sum_table.get(sum_so_far, 0) + 1
        # Recurse on our children
        paths_from_here += \
            _contiguous_subpath_in_tree_sum_sofar(end_node.left,
                                                  sum_table,
                                                  sum_so_far) + \
            _contiguous_subpath_in_tree_sum_sofar(end_node.right,
                                                  sum_table,
                                                  sum_so_far)
        # Backtrack
        sum_table[sum_so_far] -= 1
        if sum_table[sum_so_far] == 0:
            # remove ourselves from table to save space (takes O(n_nodes)
            # space down to O(height_of_tree) space
            del sum_table[sum_so_far]

        return paths_from_here

    return _contiguous_subpath_in_tree_sum_sofar(t, dict(), 0)


def main():
    # tree illustrated above
    tree1 = Node(10,                   #       10
                 Node(-2,              #      /  \
                      Node(1)),        #    -2    4
                 Node(4,               #    /    / \
                      Node(-3,         #   1    3   4
                           Node(-2)),  #       /   /
                      Node(4,          #     -2   5
                           Node(5))))  #

    # simple perfect binary trees of depth 2
    tree2 = Node(4, Node(4), Node(4))
    tree3 = Node(0, Node(0), Node(0))

    assert contiguous_subpath_in_tree_sum(tree1, 8) == 2
    assert contiguous_subpath_in_tree_sum(tree1, -2) == 2
    assert contiguous_subpath_in_tree_sum(tree1, 100) == 0
    assert contiguous_subpath_in_tree_sum(tree2, 4) == 3
    assert contiguous_subpath_in_tree_sum(tree3, 0) == 5


if __name__ == '__main__':
    main()
