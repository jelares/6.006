def reorder_students(L):
    '''
    Input:  L    | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''
    kidlen = len(L)
    mdpt = (kidlen//2)
    curr = L.head
    prev = None
    next = None

    i=0
    while curr != None:

        if i == mdpt-1:
            before_mdpt_node = curr
            curr = curr.next

        elif i == mdpt:
            next = curr.next
            curr.next = None
            prev = curr
            curr = next

        elif mdpt < i < kidlen-1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        elif i == kidlen-1:
            mdpt_node = curr
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        else:
            curr = curr.next

        i+=1

    before_mdpt_node.next = mdpt_node

    return
