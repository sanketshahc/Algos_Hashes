# TODO: Sanket Shah, ss4228

# Please see instructions.pdf for the description of this problem.
from itertools import chain
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR, EXCEPT:
    # You may add metadata fields (such as an extra integer) to help with your deletion implementation.
    # "Metadata" means that your additional fields should take O(1) space with respect to the number of entries
    # in the hash table.
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    """
    # make index from key, modulus, etc
    # if index in array is empty, throw in the pair there
    # if index is not empty, traverse the array up indices, all the way round the array,
    # like in remove fn, checking keys along the way,
    # until either:
    #   see the key-> update value
    #   get to empty spot -> throw it in there..
    # count to see if load factor met, and if so resize the table
    """
    if key is None:
      raise Exception()
    i = cs5112_hash(key) % self.array_size
    for j in chain(range(i, self.array_size), range(0, i)):
      if self.array.get(j) == None or self.array.get(j)[0] == key:
        self.array.set(j, (key, value))
        self.item_count += 1
        if self.size() > self.load_factor * self.array_size:
          self._resize_array()
        return


  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    if key is None:
      raise Exception()
    i = cs5112_hash(key) % self.array_size
    if self.array.get(i) == None:
      return None
    for j in chain(range(i, self.array_size), range(0, i)):
      if self.array.get(j)[0] == key:
        return self.array.get(j)[1]
    return None


  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    if key is None:
      raise Exception("key can not be None")
    index = cs5112_hash(key) % self.array_size
    for i in chain(range(index, self.array_size), range(0, index)):
      aval = self.array.get(i)
      if aval is not None and aval[0] == key:
        self.array.set(i, None)
        self.item_count = self.item_count - 1
        return aval[1]
    return None

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    new_hash_table = HashTable(self.array_size*2, self.load_factor)
    for i in range(0, self.array_size):
      aval = self.array.get(i)
      if aval is not None:
        new_hash_table.insert(aval[0], aval[1])
    self.array_size = self.array_size*2
    self.array = new_hash_table._get_array()

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array
