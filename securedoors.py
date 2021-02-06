n = int(input())

inside = []
while n > 0:
    dir, person = input().rstrip().split(" ")
    if dir == "entry":
        if person in inside:
            print(person + " entered (ANOMALY)")
        else:
            print(person + " entered")
            inside.append(person)
    else:
        if person in inside:
            print(person + " exited")
            inside.remove(person)
        else:
            print(person + " exited (ANOMALY)")
    n -= 1
