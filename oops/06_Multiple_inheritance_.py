class employee:
    company = "Microsoft" 
    name = "kriyan"
    def show(self):
        print(f"The name is {self.name} and the name of company is {self.company}")

class coder:
    language = "python"

    def printlanguage(self):
        print(f"The language is {self.language}")   


class programmer(employee, coder):
    company = "Fiverr"
    def showlanguage(self):
        print(f"Good in the language {self.language}")

a = employee()
b = programmer()
b.show()
b.printlanguage()
b.showlanguage()