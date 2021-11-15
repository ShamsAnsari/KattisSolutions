from math import sqrt

class Sprinkler:
    def __init__(self, x, r, start, end):
        self.x = x
        self.r = r
        self.start = start
        self.end = end

def intersection(x, r):
    # there is no intersection
    if (r**2 - (w/2)**2) < 0:
        return (-1, -1)

    start = -sqrt(r**2 - (w/2)**2) + x
    end =  sqrt(r**2 - (w/2)**2) + x
    if end > l:
        end = l
    if start < 0:
        start = 0
    return (start, end)


def compatible(curr_end, sB):
    # if sB start is inside( or at) sA and end is outside sA
    return sB.start <= curr_end and sB.end > curr_end


while True:
    try:
        n, l, w = map(int, input().split())
    except EOFError:
        break
    
    sprinklers = []


    for i in range(n):
        x, r = map(int, input().split())
        start, end = intersection(x, r)
        if start == -1 and end == -1:
            continue
        sprinkler = Sprinkler(x, r, start, end)
        
        sprinklers.append(sprinkler)

    
    
    

    #Sort by start
    sprinklers.sort(key=lambda sprinkler: sprinkler.start)

    



    covered = 0
    i = 0
    sprinklers_needed = 0
    while covered < l and i < len(sprinklers):
        best_end = covered
        
        j = i
        while j < len(sprinklers) and compatible(covered, sprinklers[j]):
            best_end = sprinklers[i].end
            j += 1
        if  j - 1 < len(sprinklers) and compatible(covered, sprinklers[j- 1]):
            sprinklers_needed += 1
        covered = best_end
        i += 1
        #print(covered)
    
    print(-1 if covered < l else sprinklers_needed)
        

     
        
        


  


