# # Use of for loop

# print("Problem 1")
# names = ["om", "shruti", "pranita", "nandini", "akshaya"]
# for val in names:
#     print(val)

# print("Problem 2")
# tup = (1, 2, 5,8 ,2,6,3,9,7,2,)
# for num in tup:
#     print(num)

# print("Problem 3")
# str = "Nandini Mahadik"
# for char in str:
#     print(char)

# #print the elements of the following list using loop
# n = [1, 4, 16, 25, 36, 49, 64, 81, 100]

# for i in n:
#     print(i)

#search for a number x in this tuple
# n = (1, 4, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36
# idx = 0
# for i in n:
#     if(x == i):
#         print("x found at index at", idx)
#     idx += 1

# # #use of range() function
# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# for i in range(2, 100, 2):
#     print(i)

# #Questions
# print("Question 1")
# for i in range(1, 101):
#     print(i)

# print("Question 2")
# for i in range(100, 0, -1):
#     print(i)

print("Question 3")
print("print the multiplication table of any number")
n = int(input("enter a number: "))
i=1
for i in range(1, 11):
    print(i*n)
