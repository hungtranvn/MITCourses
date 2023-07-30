# Implementation of sequence interface by static array.
class Array_Seq:
    def __init__(self):
        self.A = []
        self.size = 0
    def __len__(self):  return self.size
    def __iter__(self): yield from self.A # for v in seft.A yield v

    def build(self, X):
        self.A = [a for a in X] # pretend this build a static array
        self.size = len(self.A)

    def get_at(self, i): return self.A[i]
    def set_at(self, i, x): self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        """
        copy n elements of self (from index i) to A (from j)
        """
        for k in range(n):
           A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):
        """
        copy the first n elements of seft (invertical) to A (from j)
        """
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self), - 1)

# Implementation of sequence interface by Linked List
class Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    #TODO revise
    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self): return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)

# Implementation of sequence interface by dynamic array
class Dynamic_Array_Seq(Array_Seq):
    def __init__(self, r = 2):
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize()

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(len(self)): yield self.A[i]

    def build(self, X):
        for a in X: self.insert_last(a)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A)

    def _resize(self, n):
        if (self.lower < n < self.upper): return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        self.A[self.size - 1] = None
        self.size -= 1
        self.resize(self.size)

    def insert_at(self, i, x):
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.delete_last()
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

def main():
    print("Sequence Interface")

    print("Implemented by static array")
    A = Array_Seq()
    A.build([1,2,3,4,5,6,7,8])
    A.insert_first(0)
    print(A.size)
    print(A.get_at(0))

    print("Implemented by pointer-based")
    A = Linked_List_Seq()
    A.build([1,2,3,4,5])
    print(A.get_at(2))

if __name__ == "__main__":
    main()
