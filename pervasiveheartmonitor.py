try:
    while True:
        data = []
        name = ""
        line = input()
        if line == "":
            break
        line = line.rstrip().split(" ")
        for datum in line:
            try:
                data.append(float(datum))
            except ValueError:
                name += datum + " "
        avg = 0.0
        if len(data) > 0:
            avg = round(sum(data) / len(data), 4)
        print(str(avg) + " " + str(name.rstrip()))
except EOFError:
    pass
