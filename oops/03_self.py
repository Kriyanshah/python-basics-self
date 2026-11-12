class employee:
    language = "python" # this is a class attribute
    salary = 12000
    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod # no need of self parameter in static method
    def greet():
        print("Hello, Good Morning")

kriyan = employee()
kriyan.language = "javascript" # this is an instance attribute
kriyan.greet()
kriyan.getinfo()
# employee.getinfo(kriyan) 

