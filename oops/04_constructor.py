class employee:
    language = "python" # this is a class attribute
    salary = 12000


    def __init__(self, name, language, salary): # dunder method which is called automatically
        self.name = name
        self.language = language
        self.salary = salary
        print("i am creating an object")


        
    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod # no need of self parameter in static method
    def greet():
        print("Hello, Good Morning")

kriyan = employee("kriyan", "python", 12000)
print(kriyan.name, kriyan.language, kriyan.salary)

# rohan = employee()
