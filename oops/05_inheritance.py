class employee:
    company = "Microsoft" 
    name = "kriyan"
    def show(self):
        print(f"The name is {self.name} and the name of company is {self.company}")

"""class programmer:
    company = "Fiverr"
    def show(self):
        print(f"The name is {self.name} and the name of company is {self.company}")
    def showlanguage(self):
        print(f"Good in the language {self.language}")"""



class programmer(employee):
    company = "Fiverr"
    def showlanguage(self):
        print(f"Good in the language {self.language}")

a = employee()
b = programmer()
print(a.company, b.company)