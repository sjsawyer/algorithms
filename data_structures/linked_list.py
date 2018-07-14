'''
Basic linked list implementation with some common methods

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        ''' Return the value of the current node '''
        return self.value

    def get_next(self):
        ''' Return the node instance pointed to by the current node '''
        return self.next

    def set_next(self, next):
        ''' Set the node instance to be pointed to by the current node '''
        self.next = next


class Linked_list:
    '''
    A basic linked list class supporting add, pop, remove, and reverse
    methods
    '''
    def __init__(self, iterable=None):
        '''
        Note that when `Linked_list` is initialized with an iterable,
        elements are repeatedly inserted into the front of the list. As such,
        accessing will be done in a FILO manner.
        '''
        self.head = None
        if iterable is not None:
            for element in iterable:
                self.add(element)

    def add(self, value):
        ''' Add a value to the linked list by inserting at the front '''
        new_head = Node(value)
        if self.head is None:
            # we have an empty list
            self.head == new_head
        new_head.set_next(self.head)
        self.head = new_head

    def pop(self):
        ''' Remove and return the first item of the list '''
        if self.head is None:
            raise ValueError("List is empty")
        old_head = self.head
        self.head = self.head.get_next()
        return old_head.get_value()

    def remove(self, value):
        '''
        Remove the first instance of `value` in the list.
        If `value` is not in the list, `ValueError` is raised.
        '''
        prev = None
        current = self.head
        removed = False
        while current is not None:
            if current.get_value() == value:
                # Remove this node
                if prev is not None:
                    prev.set_next(current.get_next())
                else:
                    # We are removing the head node
                    self.head = current.get_next()
                removed = True
                break
            # Move on to the next node
            prev = current
            current = current.get_next()
        if not removed:
            raise ValueError("Value {} not in list".format(value))

    def reverse(self):
        ''' Reverse the list '''
        prev = None
        current = self.head
        if current is None:
            # empty list
            return current
        while current.get_next() is not None:
            self.head = current.get_next()
            current.set_next(prev)
            prev = current
            current = self.head
        # update our new head to point to the previous element
        current.set_next(prev)

    def __str__(self):
        ''' Method used to print the list '''
        l = []
        current = self.head
        while current:
            l.append(current.get_value())
            current = current.get_next()
        return str(l)


def main():
    llist = Linked_list("1234")
    print "llist: {}".format(llist)
    llist.add('a')
    print "llist.add('a'): {}".format(llist)
    llist.reverse()
    print "llist.reverse(): {}".format(llist)
    llist.remove('2')
    print "llist.remove('2'): {}".format(llist)
    val = llist.pop()
    print "llist.pop(): {}".format(repr(val))


if __name__ == '__main__':
    main()
