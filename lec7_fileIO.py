##open, read, close
#f = open("data.txt" , "r")
#data = f.read()
#data = f.read(5)
#print(type(data)
#print(data)

#reading the line by line 
# l1 =f.readline()
# print(l1) 

# l2 =f.readline()
# print(l2)



##  writing to a file
# f = open("data.txt" , "w")
# f.write("I am Nandini. Just started content creation")

# f.close() 

## apeend
# f = open("data.txt" , "a")
# f.write("\nToday I have posted my first reel. So I am little bit nervous")
# f.close() 

# #writinf in the file which is not exits already
# f2 = open("sample.txt", "w")
# f2.close()

## r+ mode
# f = open("data.txt" , "r+")
# f.write("\nHi")
# print(f.read())  #it will read from next pointer
# f.close()

## w+ mode
f = open("data.txt" , "w+")
print(f.read())  #empty output will return because file is truncated 
f.write("abbc") #printed in the file original file  
f.close()
