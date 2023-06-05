def direct_access_sort(A):
    u = 1 + max([x.key for x in A])
    D = [None] * u
    for x in A:
        D[x.key] = x
    i = 0
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i += 1

def tuple_sort(A):

def counting_sort(A):
    u = 1 + max([x.key for x in A]) # O(n)
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1

def counting_sort(A):
    u = 1 + max([x.key for x in A])
    D = [0] * u
    for x in A:
        D[x.key] += 1
    for k in range(1, u):
        D[k] += D[k-1]
    for x in list(reversed(A)):
        A[D[x.key] - 1] = x
        D[x.key] -= 1

def radix_sort(A):
    "is combined by tuple and counting sorts"
    n = len(A)
    u = 1 + max([x.key for x in A])
    c = 1 + (u.bit_length(0 // n.bit_length())
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item

def main():
if __name__=="__main__":
