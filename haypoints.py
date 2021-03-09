num_words, num_descr = map(int, input().split())

table = {}

for i in range(num_words):
    word, amount = input().split()
    amount = int(amount)
    table[word] = amount

for i in range(num_descr):
    salary = 0
    while True:
        line = input().strip()
        if line == ".":
            break
        words = line.split()
        for word in words:
            if word in table:
                salary += table[word]
    print(salary)
