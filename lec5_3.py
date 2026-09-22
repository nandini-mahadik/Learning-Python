#Search for element x in this tuple using loop 

n = (1, 4, 16, 25, 36, 49, 64, 82, 100)

i=0
x=36
while i <= len(n)-1:
    if(x == n[i]):
        print("found at index", i) #found
    
    i += 1
