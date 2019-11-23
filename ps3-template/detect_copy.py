def detect_copy(D, Q):
    '''
    Input:  D | an ASCII string 
    Output: Q | an ASCII string where |Q| < |D|
    '''
    p = 2**31 - 1

    def RP(d, p):
        magd = len(d)
        base = 128**(magd-1)
        sum = 0

        for char in d:
            sum += ord(char)*base
            base = base//128

        return sum, sum%p

    ##################
    # YOUR CODE HERE #
    ##################

    rq, rpq = RP(Q, p)
    magq = len(Q)

    base = 128**(magq-1)
    baseprime = base%p
    oteprime = 128%p

    d = D[0:magq]
    rd, rpd = RP(d, p)

    for i in range(len(D)-magq):

        if rpd == rpq:
            return True
        else:
            rpd = ((oteprime*(rpd-((ord(D[i])%p)*(baseprime))%p)%p)%p + ord(D[i+magq])%p )%p

    return False
