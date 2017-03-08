""" Based on C code from: http://nlp.cs.nyu.edu/evalb/
"""


def bracketing(ts):
    buf = range((len(ts)+1)/2 + 1)
    buf = list(reversed(zip(buf[:-1], buf[1:])))
    stack = []
    ret = []
    for t in ts:
        if t == 0:
            stack.append(buf.pop())
        elif t == 1:
            R, L = stack.pop(), stack.pop()
            stack.append((L[0], R[1]))
            if L[0] != L[1]-1:
                ret.append(L)
            if R[0] != R[1]-1:
                ret.append(R)
    ret.append(stack[-1])
    return ret


def crossing(gold, pred):
    gsplits = bracketing(gold)
    psplits = bracketing(pred)
    ret = []
    for p in psplits:
        for g in gsplits:
            if (g[0] < p[0] and g[1] > p[0] and g[1] < p[1]) or \
               (g[0] > p[0] and g[0] < p[1] and g[1] > p[1]):
               ret.append((g, p))
               break
    return ret
