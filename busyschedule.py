from datetime import datetime

result = ""
while True:
  n = int(input())

  if n == 0:
    break

  times = []
  for i in range(n):
    line = input()
    if line[-4] == "p":
      line = line.split()[0] + " " + "PM"
    else:
      line = line.split()[0] + " " + "AM"
    time = datetime.strptime(line, "%I:%M %p")
    times.append(time)

  times.sort()
  for time in times:
    time_str = time.strftime("%I:%M %p")
    if time_str[-2] == "P":
      time_str = time_str.split()[0] + " p.m."
    else:
      time_str = time_str.split()[0] + " a.m."
    result += time_str.lstrip("0") + "\n"
  result += "\n"
print(result[:-2])