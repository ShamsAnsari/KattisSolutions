line = input()
problems = line.split(";")
problems = [prob.split('-') for prob in problems]
total = 0
for problem_range in problems:
    if len(problem_range) == 1:
        total += 1
    else:
        total += int(problem_range[1]) - int(problem_range[0]) + 1
print(total)
