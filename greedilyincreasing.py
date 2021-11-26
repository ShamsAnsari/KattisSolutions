N = int(input())
A = list(map(int, input().split()))

GIS = [A[0]]
i = 1
while i < len(A):
    if A[i] > GIS[-1]:
         GIS.append(A[i])

    i += 1

print(len(GIS))
for elem in GIS:
    print(elem, end=" ")
print()

