#
# try:
#     while True:
#         line = input()
#         if line == "":
#             break
#         data = list(map(int, line.split()))
#         sum_data = sum(data)
#         for datum in data:
#             if datum == sum_data - datum:
#                 print(datum)
#                 break
# except EOFError:
#     pass


try:
    while True:
        line = input()
        if line == "":
            break
        print(sum(map(int, line.split()))//2)
except EOFError:
    pass
