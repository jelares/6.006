A = [67, 13, 49, 24, 40, 33, 58]

def h(k, c):
    return ((11*k + 4) % c) % 9

no_collision = False
c=2

while not no_collision:
    hash_domain = []
    no_collision = True
    for a in A:
        if h(a, c) in hash_domain:
            no_collision = False
            break
        else:
            hash_domain.append(h(a,c))
    if no_collision:
        print(c)
    c+=1

for a in A:
    print(h(a, 13))