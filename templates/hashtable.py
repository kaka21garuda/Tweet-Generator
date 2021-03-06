#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    # O(nk)
    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    # O(nk)
    # n: number of buckets
    # k: number of items in bucket
    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values
        pass

    # O(n) best and worst case
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    # O(1)
    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets
        return len(self.items())

    # O(n) best and worst
    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        for pair in self.items():
            if key == pair[0]:
                return True
        return False
        pass

    # O(n)
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        for pair in self.items():
            if key == pair[0][0]:
                return pair[1]
        raise KeyError
        pass

    # worst case O(n + l)
    # best case Omega(n)
    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        which_bucket = self._bucket_index(key)  # O(1)
        bucket = self.buckets[which_bucket]  # O(1)
        if self.contains(key):  # O(n)
            # worst case O(2l) for the next 4 lines
            for pair in bucket.items():  # O(l)
                if pair[0] == key:  # O(1)
                    bucket.delete(pair)  # O(l)
                    bucket.append((key, value))  # O(1)
            # print(bucket.items())
        else:
            bucket.append((key, value))  # O(1)

    # O(n)
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        which_index = self._bucket_index(key)
        for pair in self.items():
            if pair[0] == key:
                self.buckets[which_index].delete(pair)
                return
        raise KeyError
        pass


def test_hash_table():
    ht = HashTable()
    print(ht.buckets)
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
