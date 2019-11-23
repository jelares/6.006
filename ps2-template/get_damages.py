def merge_count(L, R, H, D, lenL, lenR, a, b):
    if a < b:
        if (lenR == 0) or (lenL > 0 and L[lenL-1][0] > R[lenR-1][0]):
            H[b-1] = L[lenL-1]
            lenL -= 1

            D[H[b-1][1]] += lenR
        else:
            H[b-1] = R[lenR-1]
            lenR -= 1

        merge_count(L, R, H, D, lenL, lenR, a, b-1)

def get_damages(H):
    '''
    Input:  H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    D = [1 for _ in H]
    ##################
    # YOUR CODE HERE #
    ##################

    newH = [[H[i], i] for i in range(len(H))]

    def break_down(newH, D, a=0, b=None):
        if b is None: b = len(newH)
        if 1 < b-a:
            midpoint = (a + b + 1) // 2
            break_down(newH, D, a, midpoint)
            break_down(newH, D, midpoint, b)
            L, R = newH[a:midpoint], newH[midpoint:b]
            merge_count(L, R, newH, D, len(L), len(R), a, b)

    break_down(newH, D)
    return D
