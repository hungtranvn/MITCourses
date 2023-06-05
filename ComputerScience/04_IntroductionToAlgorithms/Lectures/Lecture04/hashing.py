class DirectAccessArray:
    def __init__(self, u): self = [None] * u
    def find(self, k): return self.A[k]
    def insert(self, x): self.A[x.key] = x
    def delete(self, k): self.A[k] = None
    def find_next(self, k):
        for i in range(k, len(self.A)):
            if A[i] is not None:
                return A[i]
    def find_max(self):
        for i in range(len(self.A) - 1, -1, -1):
            if A[i] is not None:
                return A[i]
    def delete_max(self):
        for i in range(len(self.A) - 1, -1, -1):
            x = A[i]
            if x is not None:
                A[i] = None
                return x
def main():
    a = DirectAccessArray(100)

if __name__=="__main__":
    print("Hashing table")
    main()
