def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    n = len(A)
    current = 1
    length = 1
    count = 0
    ##################
    for i in range(1,n):
        # check is consecutive sequenceif A[i-1] < A[i]:
        if A[i-1] < A[i]:
            current = current + 1
        else:
            current = 1
        # update the count
        if current == length:
            count = count + 1
        elif current > length:
            length = current
            count = 1
    ##################
    return count
