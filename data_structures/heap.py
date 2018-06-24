class Heap:
    '''
    Implementation of a heap, specifically a binary, minimum heap. That
    is, the top of the heap will always be the minimum value in the heap,
    and the element at position i will always be less than those at
    positions 2*i, 2*i + 1 (we start the heap at index 1, not 0)

    '''
    def __init__(self):
        self.heap = [None, ]

    def _heap_swap(self, idx1, idx2):
        ''' utility method to swap 2 values in the heap '''
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _percolate_up(self):
        # we want to percolate up the last value in the heap
        current_idx = len(self.heap)-1
        while current_idx != 1:
            parent_idx = current_idx / 2
            if self.heap[parent_idx] > self.heap[current_idx]:
                # swap the values in the heap
                self._heap_swap(parent_idx, current_idx)
                current_idx = parent_idx
            else:
                break

    def _min_idx(self, lidx, ridx):
        if ridx < len(self.heap):
            if self.heap[ridx] < self.heap[lidx]:
                return ridx
        return lidx

    def _percolate_down(self):
        current_idx = 1
        lchild_idx, rchild_idx = 2*current_idx, 2*current_idx+1
        while lchild_idx < len(self.heap):
            # we know the current node at least has a left child
            min_idx = self._min_idx(lchild_idx, rchild_idx)
            if self.heap[current_idx] > self.heap[min_idx]:
                self._heap_swap(current_idx, min_idx)
                current_idx = min_idx
                lchild_idx, rchild_idx = 2*current_idx, 2*current_idx+1
            else:
                break

    def __str__(self):
        return str(self.heap[1:])

    def __len__(self):
        return len(self.heap)-1

    def push(self, val):
        self.heap.append(val)
        self._percolate_up()

    def pop(self):
        ret = self.heap[1]
        # replace first element with the last
        self.heap[1] = self.heap.pop()
        self._percolate_down()
        # return the original top value
        return ret


def main():
    heap = Heap()
    values = [6, 2, 4, 5, 9, 3, 10, 7]
    for val in values:
        heap.push(val)
    print heap
    print "Popping {}".format(heap.pop())
    print heap


if __name__ == '__main__':
    main()
