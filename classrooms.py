from sys import stdin
import bisect


def compatible(activity, classroom):
    if classroom == 0:
        return True
    # Activity must start after last class
    return classroom < activity[1] 

def bubble(i, array):

    while i < len(array) - 1 and array[i + 1] < array[i]:
        array[i], array[i + 1] = array[i + 1], array[i]
        i += 1
    while i > 0 and array[i - 1] > array[i]:
        array[i], array[i - 1] = array[i - 1], array[i]
        i -= 1
    



fast_input =  lambda : stdin.readline().strip()

num_activities, num_classrooms = map(int, fast_input().split())

classrooms = [0] * num_classrooms


activities = []
for i in range(num_activities):
    s_i, f_i = map(int, fast_input().split())
    activities.append((f_i, s_i))
    

activities.sort()
num_possible_act = 0


for activity in activities:
    i = bisect.bisect_left(classrooms, activity[1]) - 1
    if compatible(activity, classrooms[i]):
        classrooms[i] = activity[0]
        bubble(i, classrooms)
        num_possible_act += 1

print(num_possible_act)