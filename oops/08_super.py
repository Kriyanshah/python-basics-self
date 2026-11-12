class employee:
    def __init__(self):
        print("Constructor of employee")
    a =1
class programmer(employee):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")
    b = 2
class coder(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of coder")
    c = 3

o = coder()

print(o.a,o.b,o.c)