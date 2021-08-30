def is_duplicate(names, person, key):
    for name in names:
        if key(name) == key(person):
            return True
    return False

first = lambda x: x[0]
last = lambda x: x[1]

names = []
duplicates = []
try:
    while True:
        person = input().split()
        if person == []:
            break
        if is_duplicate(names, person, first):
            duplicates.append(first(person))
        names.append(person)
except EOFError:
    pass
names.sort(key=first)
names.sort(key=last)


for person in names:
    if first(person) in duplicates:
        print(first(person), last(person))
    else:
        print(first(person))
