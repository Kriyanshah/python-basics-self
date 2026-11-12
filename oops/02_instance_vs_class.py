class employee:
    language = "python" # this is a class attribute
    salary = 12000

kriyan = employee()
kriyan.language = "javascript" # this is an instance attribute
print(kriyan.language, kriyan.salary)

# instance is preferred over class attribute if both have same name
