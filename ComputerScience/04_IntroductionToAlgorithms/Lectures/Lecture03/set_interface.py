import sys
sys.path.insert(0,"../Lecture2")
from sequence_interface import Array_Seq

# set interface implementation
class Sorted_Array_Set:
    def __init__(self): self.A = Array_Seq()
    
    def __len__(self): return len(self.A)
    
    def __iter__(self): yield from self.A
    
    def iter_order(self): yield from self
    
    def build(self, X):
        self.A.build(X)
        self._sort()

    def _sort(self):
        for i in range(1, len(self.A)):
            j = i
            while j > 0 and self.A[j].key < self.A[j - 1].key:
                self.A[j - 1], self.A[j] = self.A[j], self.A[j - 1]
                j = j - 1

    def _binary_search(self, k, i, j):
        if i >= j: return i
        m = (i + j)  // 2
        x = self.A.get_at(m);
        if k < x.key: return self._binary_search(k, i, m - 1)
        if k > x.key: return self._binary_search(k, m + 1, j)
        return m

    def find_min(self):
        if len(self) > 0: return self.A.get_at(0)
        else: return None

    def find_max(self):
        if len(self) > 0: return self.A.get_at(len(self) - 1)
        else: return None

    def find(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k: return x
        else: return None

    def find_next(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key > k: return x
        if i > 0: return self.A.get_at(i + 1)
        else: return None

    def find_prev(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < k: return x
        if i > 0: return self.A.get_at(i - 1)
        else: return None

    def insert(self, x):
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self.A) - 1)
            k = self.A.get_at(i).key
            if k == x.key:
                self.A.set_at(i, x)
                return False
            if k > x.key: self.A.insert_at(i, x)
            else: self.A.insert_at(i + 1, x)
        return True

    def delete(self, k):
        i = self._binary_search(k, 0, len(self) - 1)
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)

# sorting

# selection sort
def selection_sort(A, i = None):
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i - 1)

def prefix_max(A, i):
    if i > 0:
        j = prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
    return i

# insertion sort
def insertion_sort(A, i = None):
    if i is None: return len(A) - 1
    if i > 0:
        insertion_sort(A, i - 1)
        insert_last(A, i)

def insert_last(A, i):
    if i is None: return i
    if i > 0:
        if A[i - 1] > A[i]:
            A[i - 1], A[i] = A[i], A[i - 1]
        insert_last(A, i - 1)

# merge sort
def merge_sort(A, a = 0, b = None):
    print("merge sort")
    if b is None: b = len(A)
    
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        i, j = 0, 0
        while a < b:
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                A[a] = L[i]
                i = i + 1
            else:
                A[a] = R[j]
                j = j + 1
            a = a + 1

def main():
    print("main function")

    print("test find max")
    A = [1,3,6,7,9,0,2,5]
    print(prefix_max(A, len(A) - 1))

    print("test merge sort")
    merge_sort(A)
    print(A)



if __name__ == "__main__":
    main()
