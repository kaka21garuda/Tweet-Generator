#!python

from __future__ import print_function
import sys

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.count = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        return self.count
        pass

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item
        new_node = Node(data=item)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
            pass

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(data=item)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        start_node = self.head
        before_node = None
        # iterate through all the nodes in the object
        while start_node:
            # if the item is found in the data
            if start_node.data == item:
                # if there is a node before the start node
                if before_node:
                    if start_node.next is None:
                        self.tail = self.head
                    before_node.next = start_node.next
                elif before_node is None and start_node.next is None:
                    self.head = None
                    self.tail = None
                elif before_node is None:
                    self.head = start_node.next
                # decrement the amount of node by 1
                self.count -= 1
                return True
            else:
                before_node = start_node
                start_node = before_node.next
        else:
            # raise a ValueError when to
            raise ValueError
            pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        start_node = self.head
        while start_node:
            if start_node:
                if quality(start_node.data) is True:
                    return start_node.data
                else:
                    start_node = start_node.next
        else:
            return None
            

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
