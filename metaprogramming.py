definitions = {}
try:
    while True:
        line = input()
        line = line.split()
        if line[0] == "define":
            definitions[line[2]] = int(line[1])
        elif line[1] in definitions and line[3] in definitions:
            if line[2] == "=":
                print("true" if definitions[line[1]] == definitions[line[3]] else "false")
            elif line[2] == ">":
                print("true" if definitions[line[1]] > definitions[line[3]] else "false")
            elif line[2] == "<":
                print("true" if definitions[line[1]] < definitions[line[3]] else "false")
            else:
                print("undefined")
        else:
            print("undefined")
except EOFError:
    pass
