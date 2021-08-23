def count_occurances(S, L):
    '''
    Count occurances of S in L with overlapping
    '''
    occurance_count = 0
    i, j = 0, len(S)
    while j <= len(L):
        s = L[i:j]
        if s == S:
            occurance_count += 1
        i, j = i + 1, j + 1
    return occurance_count


while True:
    line = input().split()
    if line[0] == "0":
        break
    S, L = line

    # TYPE 1
    type1 = count_occurances(S, L)


    # TYPE 2
    type2 = 0
    unique_remove_one = set()
    n = len(S)
    for i in range(n):
        s = S[:i] + S[i + 1:]
        unique_remove_one.add(s)
    for e in unique_remove_one:
        #type2 += L.count(e)
        type2 += count_occurances(e, L)

    # TYPE 3
    type3 = 0
    letters = ['A', 'G', 'C', 'T']

    unique_add_one = set()
    for l in letters:
        for i in range(n+1):
            s = S[:i] + l + S[i:]
            unique_add_one.add(s)
    for e in unique_add_one:
        #type3 += L.count(e)
        type3 += count_occurances(e, L)

    print(type1, type2, type3)
