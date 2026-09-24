# #recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)


# #calculating factorial using recursion
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

# #write a recursive function to calculate the sum of first n natural numbers
# def cal_sum(n):
#     if(n==0):
#         return 0

#     return cal_sum(n-1) + n
# sum = cal_sum(5)
# print(sum)

#write a recursive function to print all elements in a list
#Hint :  use list and index as a parameter

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

letters = ['a','b','c','d','e']
print_list(letters)