def min_time(C, D):
    '''
    Input:  C | a list of code pairs
            D | a list of dependency pairs
    Output: t | the minimum time to complete the job, 
                or None if the job cannot be completed
    '''
    t = None
    ##################
    # YOUR CODE HERE #
    ##################

    # Fully build adj list representation of graph
    adj = []
    names = {}
    times = {}
    i = 0
    for c in C:
        names[c[0]] = i
        times[i] = -c[1]
        adj.append([])
        i += 1

    for d in D:
        f1, f2 = d
        adj[names[f1]].append((names[f2], times[names[f1]]))


    def relax(adj, time, d, parent, u, v):
        if d[v] > d[u] + time:
            d[v] = d[u] + time
            parent[v] = u


    def dfs(adj, s, parent=None, order=[], rec_stack=None, cyclic=False):  # Adj: adjacency list, s: start

        if parent is None:  # O(1) initialize parent list
            parent = [None for v in adj]  # O(V) (use hash if unlabeled)
            parent[s] = s  # O(1) root

        if rec_stack == None:
            rec_stack = [False for _ in adj]

        rec_stack[s] = True

        for v in adj[s]:  # O(Adj[s]) loop over neighbors
            node = v[0]
            if rec_stack[node]:
                cyclic = True
            elif parent[node] is None:  # O(1) parent not yet assigned
                parent[node] = s  # O(1) assign parent
                _, _, cyclic = dfs(adj, node, parent, order, rec_stack, cyclic)  # Recursive call

        rec_stack[s] = False
        order.append(s)  # O(1) amortized
        return parent, order, cyclic


    def full_dfs(adj):  # Adj: adjacency list
        parent = [None for v in adj]  # O(V) (use hash if unlabeled)
        order = []  # O(1) initialize order list
        rec_stack = [False for _ in adj]
        cyclic = False

        for v in range(len(adj)):  # O(V) loop over vertices
            if parent[v] is None:  # O(1) parent not yet assigned
                parent[v] = v  # O(1) assign self as parent (a root)
                _, _, cyclic = dfs(adj, v, parent, order, rec_stack, cyclic)  # DFS from v (BFS can also be used)

        return parent, order, cyclic


    def dag_sp(adj, times, parent, order):
        d = [0 if parent[i] == i else float('inf') for i in range(len(parent))]
        # print(d)

        for u in order:
            for v in adj[u]:
                node = v[0]
                time = v[1]
                relax(adj, time, d, parent, u, node)

        return d, parent


    def find_max_time(d, times):
        minpath = 0
        mintime = 0
        maxel = None

        for i in range(len(d)):
            if d[i] < minpath:
                minpath = d[i]

        for i in range(len(d)):
            if d[i] == minpath:
                if times[i] < mintime:
                    mintime = times[i]

        return -(minpath+mintime)


    parent, order, cyclic = full_dfs(adj)
    order.reverse()

    if cyclic:
        return None

    d, parent = dag_sp(adj, times, parent, order)
    t = find_max_time(d, times)

    # print(cyclic)
    # print(t)
    # print(d,"\n",parent)
    # print(parent,"\n",order)
    # print(adj)
    # print(C,"\n",D)
    return t
