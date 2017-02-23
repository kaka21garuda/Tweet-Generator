#!python

from __future__ import print_function

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

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of item
        return self.count
        pass

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item

        # making a new_node
        new_node = Node(data=item)
        # if there is no any node in the linkedlist
        if self.count == 0:
            # assign the head with the new_node
            self.head = new_node
            # assign the tail with the new_node
            self.tail = new_node
            self.count += 1
        else:
            # make the new_node of the tail.next
            # meaning it will be the element after latest element
            self.tail.next = new_node
            # assign a new tail with the new_node
            self.tail = new_node
            self.count += 1
            pass

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # make a node
        new_node = Node(data=item)
        if self.count == 0:
            # if there is no node in the linkedlist
            # make the new_node as the head
            self.head = new_node
            # also its tail
            self.tail = new_node
            self.count += 1
        else:
            # if there's already a new_node
            # prepend the head of linkedlist after the new_node
            new_node.next = self.head
            # assign the head with the new_node
            self.head = new_node
            self.count += 1
            pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found

        node = self.head
        before_node = None
        # iterate through all the nodes in the object
        while node:
            # if the item is found in the data
            print("Node:", node)
            if node.data == item:
                # if there is a node before the start node
                print("before_node:", before_node)
                print("node.next:", node.next)
                if before_node:
                    if node.next is None:  # if node == self.tail
                        self.tail = before_node
                    before_node.next = node.next
                elif before_node is None and node.next is None:
                    self.head = None
                    self.tail = None
                elif before_node is None:
                    self.head = node.next
                # decrement the amount of node by 1
                self.count -= 1
                return
            else:
                before_node = node
                node = before_node.next
        # raise a ValueError when to
        raise ValueError

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True

        start_node = self.head
        # start from the head
        while start_node:
            # start iterating the node from the head
            # start_node is not None
            if start_node:
                if quality(start_node.data) is True:
                    # return the start_node.data if its True in quality
                    return start_node.data
                else:
                    # if not True
                    # set the start_node into the next one
                    start_node = start_node.next
        else:
            return None
            pass


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')

    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))

    print(ll.length())

    # ll.delete('A')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('B')
    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    # print(ll.length())
    # print('length: ' + str(ll.length()))

    # Enable this after implementing delete:
    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
