class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod # No need to pass self argument
    def greet():
        print("Good Morning , Sir")

    @staticmethod # No need to pass self argument
    def time():
        print("The time is good")


harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry,"Thanks!") , Can pass more arguments , "Thanks! will go in Signature"
harry.greet() # Employee.greet()
harry.time()

