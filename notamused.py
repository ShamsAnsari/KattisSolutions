result = ""
day = 0
while True:
  line = ""
  try:
    line = input()
  except EOFError:
    break
    
  if line == "":
    break
  if line == "OPEN":
    day += 1
    logs = {}
    while True:
      line = input().split()
      if line[0] == "CLOSE":
        break
      elif line[0] == "ENTER":
        name = line[1]
        time = int(line[2])
        if name in logs:
          logs[name].append(time)
        else:
          logs[name] = [time]
      elif line[0] == "EXIT":
        name = line[1]
        time = int(line[2])
        logs[name].append(time)
  result += f'Day {day}\n'
  for key in sorted(logs):
    time_logs = logs[key]
    amount_due = 0
    for i in range(0, len(time_logs), 2):
      amount_due += (time_logs[i + 1] - time_logs[i]) * 0.10
    result += f"{key} ${amount_due:.2f}\n"
  result += "\n"

print(result[:-2])


    
