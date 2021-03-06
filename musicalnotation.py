"""
G:
F: ----------------------------------------------------------
E:
D: ----------------------------------------------------------
C:
B: ----------------------------------------------------------
A:
g: ----------------------------------------------------------
f:
e: ----------------------------------------------------------
d:
c:
b:
a: ----------------------------------------------------------
"""

letters = ["G", "F", "E", "D", "C", "B", "A", "g", "f", "e", "d", "c", "b", "a"]
dashs = [1, 3, 5, 7, 9, 13]
sheet = [None] * 14
for i in range(len(sheet)):
    sheet[i] = [letters[i], ":", " "]

n = int(input())
data = input().split()

for datum in data:
    letter = datum[0]
    beat = 1
    if len(datum) > 1:
        beat = int(datum[1])

    for i in range(len(sheet)):
        if i == letters.index(letter):
            sheet[i].extend("*" * beat)
        elif i in dashs:
            sheet[i].extend("-" * beat)
        else:
            sheet[i].extend(" " * beat)

        if i in dashs:
            sheet[i].extend("-")
        else:
            sheet[i].extend(" ")

#trim
for i in range(len(sheet)):
    sheet[i].pop()

for i in range(len(sheet)):
        print(''.join(sheet[i]))
