def calculate(lst):
    M = max(lst)
    N = min(lst)
    return N, M, M - N

case = 1
while True:
    try:
        line = input()
    except EOFError:
        break
    
    print(f'Case {case}:', *calculate(list(map(int, line.split()))[1:]))
    case +=1 