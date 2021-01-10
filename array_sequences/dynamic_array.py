import ctypes
import sys


class DynamicArray(object):
    """Implementation of a dynamic array"""
    def __init__(self):
        self.n = 0 # count of elements
        self.capacity = 1 # accepts only 1 element by default
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        """Return element at index k"""

        if not 0 <= k < self.n:
            return IndexError('K is out of range/bounds')
        return self.A[k]

    def append(self, el):
        """Add to end of the array"""
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough
        self.A[self.n] = el
        self.n += 1

    def _resize(self, new_cap):
        """Resize current array to the capacity of the new_cap"""
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k] # adding all existing values from A into B

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        """Makes a raw array - returns new array with a new capacity"""
        return (new_cap * ctypes.py_object)() # grabbing raw bytes and creating an array

    def __getsize__(self):
        """Get bytes/size of arr"""
        return sys.getsizeof(self.A)


arr = DynamicArray()
arr.append(1)
print(arr.__getsize__())
arr.append(2)
print(arr.__getsize__())
arr.append(3)
print(arr.__getsize__())
#print(len(arr))
#print(arr.__getitem__(2))
