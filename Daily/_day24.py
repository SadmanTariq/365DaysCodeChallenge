def rational2continued(n, d):
    q = int(n/d)
    r = n % d
    if r == 0:
        return [q]
    else:
        return [q] + rational2continued(d, r)

def continued2rational(c):
    if type(c[1]) == int:
        return c
    else:
        # return [c[1][1], c[0] * c[1][1] + c[1][0]]
        c[1] = continued2rational(c[1])
        return [c[1][1], c[0] * c[1][1] + c[1][0]]

def decrypt(n, d):
    return "".join([chr(x) for x in rational2continued(n, d)])

# print(decrypt(368404499498850749308034650200269509714103204, 4911485647420182652636995197665952062862792))

def to_linked_list(l):
    new_list = []
    for e in l:
        new_list += [e, 1]
    new_list.pop()
    
    head = [new_list[0]]
    cur = head
    for a in new_list[1:]:
        cur.append([a])
        cur = cur[1]

    cur.append(1)
    return head

print(continued2rational(to_linked_list([97, 100, 111, 98, 101])))
