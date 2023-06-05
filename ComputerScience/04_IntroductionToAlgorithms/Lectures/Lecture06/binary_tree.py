class Binary_Node(object):
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
    def subtree_iter(A):
        """
        Traversal order
        """
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()
    def subtree_first(A):
        """
        Find the first node
        """
        if A.left: return A.left.subtree_first()
        else: return A
    def subtree_last(A):
        """
        Find the last node
        """
        if A.right: return A.right.subtree_last()
        else: return A
    def successor(A):
        """
        Find the node just after node A
        """
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    def predecessor(A):
        """
        Find the node just before node A
        """
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        # A.maintain()
    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        # A.maintain()
    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            # A.parent.maintain()
        return A

class Binary_Tree(object):
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type
    def __len__(T): return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item
    def build(X):
        A = [x for x in X]
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c:
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root
        self.root = build_subtree(A, 0, len(A) - 1)
    def tree_iter(T):
        node = T.subtree_first()
        while node:
            yield node
            node = node.successor()

class BST_Node(Binary_Node):
    def subtree_find(A, k):
        if k < A.item.key:
            if A.left:  return A.left.subtree_find(k)
        elif k > A.item.key:
            if A.right: return A.right.subtree_find(k)
        else:   return A
        return None
    def subtree_find_next(A, k):
        if A.item.key <= k:
            if A.right: return A.right.subtree_find_next()
            else:   return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B:   return B
        return A
    def subtree_find_prev(A, k):
        if A.item.key >= k:
            if A.left:  return  A.left.subtree_find_prev(k)
            else:   return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:   return B
        return A
    def subtree_insert(A, B):
        if B.item.key < A.item.key:
            if A.left: A.left.subtree_insert(B)
            else:   A.subtree_insert_before(B)
        elif B.item.key >  A.item.key:
            if A.right: A.right.subtree_insert(B)
            else:   A.subtree_insert_after(B)
        else:   A.item = B.item

class Set_Binary_Tree(Binary_Tree):
    def __init__(self): super().__init__(BST_Node)
    def iter_order(self): yield from self
    def build(self, X):
        for x in X: self.insert(x)
    def find_min(self):
        if self.root:   return self.root.subtree_first().item
    def find_max(self):
        if self.root:   return self.root.subtree_last().item
    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node: return node.item
    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:    return node.item
    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node
        self.size += 1
        return True
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None:  self.root = None
        self.size -= 1
        return ext.item

if __name__=="__main__":
    print("Test a binary tree")
    T = Binary_Tree()
    X = [0,1,2,3,4,5,6,7,8,9]
    T.build(X)
