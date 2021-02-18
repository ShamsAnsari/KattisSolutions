"""
All logic is correct.
This kattis problem has tedious parsing problem
Kattis doesnt Accept
"""


def check_injective(data):
    codomain = []
    for k, v in data.items():
        if v in codomain:
            return False
        codomain.append(v)

    return True


def check_surjective(data, codomain):
    for element in codomain:
        if element not in data.values():
            return False
    return True


def get_type(data, codomain):
    is_injective = check_injective(data)
    is_surjective = check_surjective(data, codomain)

    if is_injective and not is_surjective:
        return "injective"
    if is_surjective and not is_injective:
        return "surjective"
    if is_surjective and is_injective:
        return "bijective"
    return "neither injective nor surjective"


def get_data(n):
    data = {}

    for i in range(n):
        datum = input().strip().split(" ")
        if datum[0] in data:
            return None
        data[datum[0]] = datum[-1]

    if len(data) == 0:
        return None
    return data



try:
    while True:
        domain = input()
        if domain == "":
            break

        domain = domain.split()[1:]
        codomain = input().split()[1:]

        n = int(input().strip())#PROBLEM, tedious parsing problem. This line

        data = get_data(n)
        if data is None:
            print("not a function")
            continue
        print(get_type(data, codomain))
except EOFError:
    pass
