#Dictionary and Set in Python
# #Q1
# words = {
#     "table" : ("a piece of furniture", "lists of facts and figures"),
#     "cat" : "a small animal"
# }
# print("Created dictionary is: ", words)


# #Q2
# You are given a list of subjects fo students. Assume one clasroom is
# required for 1 subject. How many classrooms are needed by all students.
# stud = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(len(stud))
# print(stud)

#Q3
# dictionary = {}
# mark1 = int(input("enter marks: "))
# mark2 = int(input("enter marks: "))
# mark3 = int(input("enter marks: "))
# mark4 = int(input("enter marks: "))
# dictionary.update({"phy" : mark1})
# dictionary.update({"chem" : mark2})
# dictionary.update({"math" : mark3})
# dictionary.update({"python" : mark4})
# print(dictionary)


#Q4
#figyure out the way to store 9 and 9.0 as separate values in set
val1 = {9, 9.0}
print(val1)

#way1
val2 = {9, "9.0"}
print(val2)

#way2
val3 = {
    ("float", 9.0),
    ("int", 9)
}
print(val3)