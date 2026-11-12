class employee:
    a =1
class programmer(employee):
    b = 2
class coder(programmer):
    c = 3
o = employee()
print(o.a) # prints the a attribute of employee class
# print(o.b) # throws an error because b attribute is not present in employee class
p = programmer()
print(p.a) # prints the a attribute of employee class
print(p.b) # prints the b attribute of programmer class

c = coder()
print(c.a) # prints the a attribute of employee class
print(c.b) # prints the b attribute of programmer class
print(c.c) # prints the c attribute of coder class