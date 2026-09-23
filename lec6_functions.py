# #function definition
# def sum(a,b): #passing parameters
#     s = a+b   #calculation sum
#     print(s)  
#     return s  #returns the result
# sum(4,5) #calling the function as many times you want
# sum(8,10)
# sum(9,20)


# #WAP to print length of the list
# cities = ["delhi", "pune", "mumbai" , "chennai"]
# nums =[1,4,9,43,765, 78, 80, 200]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(nums)

#WAF to print the elements of a list in a single line(list is a parameter)
# cities = ["delhi", "pune", "mumbai" , "chennai"]
# nums =[1,4,9,43,765, 78, 80, 200]
# def print_list(list):
#     for i in list:
#         print(i, end=" ")
# print_list(cities)
# print_list(nums)

# #WAF to find the factorial of n (n is the parameter)
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# factorial(5)
# factorial(8)
# factorial(7)

#WAF to convert USD in INR 1$ = 83 rs
def convert(num):
    result = num * 83 #inr = usd * 83
    print(result)

convert(5)
convert(19)
