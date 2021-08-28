

def lst_to_str(lst):
    result = ""
    for e in lst:
        result += str(e) + " "
    return result[:-1]

def lst_to_str_rec(lst):
    if len(lst) == 1:
        return lst_to_str(lst[0]) + "\n"
    else:
        return lst_to_str(lst[0]) + "\n" + lst_to_str_rec(lst[1:])



attrs = input().split()
num_songs = int(input())

songs = []
for i in range(num_songs):
    song = input().split()
    songs.append(song)

num_sorts = int(input())
sorting_order = [input() for _ in range(num_sorts)]

result = ""

for attr in sorting_order:
    attr_index = attrs.index(attr)
    songs.sort(key=lambda song: song[attr_index] )
    result += lst_to_str(attrs) + "\n"
    result += lst_to_str_rec(songs) + "\n"

print(result[:-2])
