def c(S,U):
    import itertools as i
    for l in range(len(S)):
        for s in i.combinations(S,l+1):
            if set.union(*s)==U:return s
