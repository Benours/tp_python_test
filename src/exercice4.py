def index_minimum( t, d, f):
    index_min = d
    for i in range(d + 1, f + 1):
        if t[i] < t[index_min]:
            index_min = i
    return index_min

def tri_a_bulles( t):
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j + 1] < t[j]:
                t[j + 1], t[j] = t[j], t[j + 1]
    return t

def find_in_sort_tab( t, e):
    for i in range(len(t)):
        if t[i] == e:
            return i
    return "WARN: Element non trouvé"

def find_dichotomique( t, e):
    d = 0
    f = len(t) - 1
    while d <= f:
        m = (d + f) // 2
        if t[m] == e:
            return m
        elif t[m] < e:
            d = m + 1
        else:
            f = m - 1
    return "WARN: Element non trouvé"

def insertion( e, t, n):
    i = n - 2
    while i >= 0 and t[i] > e:
        t[i + 1] = t[i]
        i -= 1
    t[i + 1] = e
    return t

def tri_extraction( t):
    for i in range(len(t) - 1):
        index_min = index_minimum(t, i, len(t) - 1)
        t[i], t[index_min] = t[index_min], t[i]
    return t

def tri_insertion( t):
    for i in range(1, len(t)):
        insertion(t[i], t, i + 1)
    return t
