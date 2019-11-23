def min_mod_tuple(A, k):
    ##################
    # Your Code Here #
    ##################

    min_i = 0
    min_j = 1

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            current_mod = (A[i]*A[j]) % k

            try:
                if current_mod < min_mod:
                    min_mod = current_mod
                    min_i = i
                    min_j = j
            except:
                min_mod = current_mod

    return (min_i, min_j)
