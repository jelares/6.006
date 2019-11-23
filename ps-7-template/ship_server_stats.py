def ship_server_stats(R, s, t):
    '''
    Input:  R | a list of route tuples
            s | string name of origin city
            t | string name of destination city
    Output: w | maximum weight shippable from s to t
            c | minimum cost to ship weight w from s to t
    '''
    w, c = 0, 0
    ##################
    # YOUR CODE HERE #
    ##################

    # make the priority queue class
    class PriorityQueue:  # Hash Table Implementation

        def __init__(self):  # stores keys with unique labels
            self.A = {}

        def __contains__(self, item):
            for a in self.A.keys():
                if a == item:
                    return True
            return False

        def insert(self, label, key):  # insert labeled key
            self.A[label] = key

        def extract_min(self):  # return a label with minimum key
            min_label = None
            for label in self.A:
                    if (min_label is None) or (self.A[label] < self.A[min_label]):
                        min_label = label
            del self.A[min_label]
            return min_label

        def extract_max(self):  # return a label with maximum key
            max_label = None
            for label in self.A:
                    if (max_label is None) or (self.A[label] > self.A[max_label]):
                        max_label = label
            del self.A[max_label]
            return max_label

        def decrease_key(self, label, key):  # decrease key of a given label
            if key < self.A[label]:
                self.A[label] = key

        def increase_key(self, label, key):
            if key > self.A[label]:
                self.A[label] = key

    # build the graphs
    names_to_nums ={}
    weight_graph = {}
    cost_graph = {}

    i = 0
    for r in R:

        if r[0] in names_to_nums and r[1] in names_to_nums:
            weight_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[2]))
            cost_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[3]))

        elif r[0] in names_to_nums:
            names_to_nums[r[1]] = i
            weight_graph[names_to_nums[r[1]]] = []
            cost_graph[names_to_nums[r[1]]] = []
            i += 1

            weight_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[2]))
            cost_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[3]))

        elif r[1] in names_to_nums:
            names_to_nums[r[0]] = i
            weight_graph[names_to_nums[r[0]]] = []
            cost_graph[names_to_nums[r[0]]] = []
            i += 1

            weight_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[2]))
            cost_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[3]))

        else:
            names_to_nums[r[0]] = i
            weight_graph[names_to_nums[r[0]]] = []
            cost_graph[names_to_nums[r[0]]] = []
            i += 1
            names_to_nums[r[1]] = i
            weight_graph[names_to_nums[r[1]]] = []
            cost_graph[names_to_nums[r[1]]] = []
            i += 1

            weight_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[2]))
            cost_graph[names_to_nums[r[0]]].append((names_to_nums[r[1]], r[3]))

    def relax_b(b, v, u, w):
        if b[v] < min(b[u], w):
            b[v] = min(b[u], w)

    def djikstra_b(adj, s):
        b = [float('-inf') for _ in adj]
        b[s] = float('inf')
        q = PriorityQueue()

        for v in range(len(adj)):
            q.insert(v, b[v])

        for _ in range(len(adj)):
            u = q.extract_max()
            for v_info in adj[u]:
                v = v_info[0]
                w = v_info[1]
                if v in q:
                    relax_b(b, v, u, w)
                    q.increase_key(v, b[v])
        return b

    def relax(d, v, u, w, parent):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    def djikstra(adj, s):
        d = [float('inf') for _ in adj]
        parent = [None for _ in adj]
        d[s], parent[s] = 0, s
        q = PriorityQueue()

        for v in range(len(adj)):
            q.insert(v, d[v])

        for _ in range(len(adj)):
            u = q.extract_min()

            for v_info in adj[u]:
                v = v_info[0]
                w = v_info[1]

                if v in q:
                    relax(d, v, u, w, parent)
                    q.decrease_key(v, d[v])

        return d, parent

    sf = names_to_nums['San Fransisco']
    cm = names_to_nums['Cambridge']

    b = djikstra_b(weight_graph, sf)
    cost_graph = {}

    for r in R:
        s = names_to_nums[r[0]]
        t = names_to_nums[r[1]]
        w = r[2]
        c = r[3]

        if s not in cost_graph.keys():
            cost_graph[s] = []

        if t not in cost_graph.keys():
            cost_graph[t] = []

        if w >= b[cm]:
            cost_graph[s].append((t, c))

    d, parent = djikstra(cost_graph, sf)
    c = d[cm]
    w = b[cm]

    # print(sf," ", cm)
    # print(b[cm])
    # print(weight_graph)
    # print(cost_graph)
    # print(w, " ", c)
    return w, c
