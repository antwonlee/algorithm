p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)

    print "----- sum of all q to normalize ------"
    print s

    for i in range(len(q)):
        q[i] = q[i] / s

    print "----- normalized q's ------"
    print q
    one = sum(q)
    print one
    return q

print sense(p, Z)
