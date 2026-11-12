class employee:
    a = 1
    @classmethod  # Decorator
    def show(cls):
        print(f"the class attribute is: {cls.a}")
e = employee()
e.a = 45
e.show() # this will print the class attribute because class method is used