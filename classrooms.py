from heapq import *
from sys import stdin
import bisect

def compatible(activity, classroom):
    if classroom == 0:
        return True
    # Activity must start after last class
    return classroom < activity[1] 


fast_input =  lambda : stdin.readline().strip()
num_activities, num_classrooms = map(int, fast_input().split())

classrooms = [0] * num_classrooms


activities = []
for i in range(num_activities):
    s_i, f_i = map(int, fast_input().split())
    heappush(activities, (f_i, s_i))
    


num_possible_act = 0
while len(activities) > 0:
    activity = heappop(activities)
    i = bisect.bisect_right(classrooms, activity[1]) - 1
    while i >= 0:
        if compatible(activity, classrooms[i]):
            del classrooms[i]
            j = bisect.bisect_left(classrooms, activity[0]) 
            classrooms.insert(j, activity[0])
            num_possible_act += 1
            break
        i -= 1

print(num_possible_act)