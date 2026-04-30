class employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("Employee's to do the work")
class manager(employee):
    def work(self):
        print(self.name,"The manager manages the team")
class tester(employee):
    def work(self):
        print(self.name,"The tester tests the code")
    def employe_details(emp):
        emp.work()
m=manager("GIRLS")
t=tester("BOYS")
employee.details(m)
employee.details(t)
    
    
