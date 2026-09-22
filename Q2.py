#USe of break and continue

#break keyword : used to terminate the loop when encountered
print("Solution 1")
n = (1, 4, 16, 25, 36, 49, 64, 82, 100)
i=0
x=36
while i <= len(n)-1:
    if(x == n[i]):
        print("found at index", i) #found
        break  #here at idx 4 the loop will terminate 
    else:
        print("searching")
    i += 1
print("end of loop")


#continue keyword : terminates execution in current iteration and continues from next iteration
print("Solution 2")
i = 0
while i <= 5:
    if(i == 3):
        i+=1
        continue #skip 
    print(i)
    i+=1

#printing odd numbers btn 1 to 10
print("Solution 3")
i = 1
while i <= 10:
    if(i%2 == 0):
        i +=1
        continue
    print(i)
    i += 1