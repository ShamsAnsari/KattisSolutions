common_word = input()
num_lists = int(input())



endings = set()
for _ in range(num_lists):
    lst = input().split()
    for ending in lst:
        if ending == common_word[-len(ending):]:
            endings.update(lst)
            break
    

num_phrases = int(input())
phrases = []
for _ in range(num_phrases):
    phrases.append(input().split())


for phrase in phrases:
    last_word = phrase[-1]
    found = 'NO'
    for i in range(len(last_word)):
        if last_word[-i:] in endings:
            found = 'YES'
    print(found)

            
    




