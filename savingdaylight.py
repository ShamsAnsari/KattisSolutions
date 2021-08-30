from datetime import datetime

def hours_minutes(td):
    return  td.seconds//3600, (td.seconds//60)%60
try:
  while True:
    line = input()
    month, day, year, sunrise, sunset = line.split()
    sunrise =  datetime.strptime(sunrise, "%H:%M")
    sunset = datetime.strptime(sunset, "%H:%M")
    time_sunlight = sunset - sunrise
    hours, minutes = hours_minutes(time_sunlight)
    print(f'{month} {day} {year} {hours} hours {minutes} minutes')
except EOFError:
  pass
