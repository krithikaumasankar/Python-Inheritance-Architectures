#EMPLOYEE SALARY CALCULATION
# Base Class
class Employee:
    def __init__(self, emp_id, name, salary, percentage):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.percentage = percentage

    def calculate_bonus(self):
        bonus = (self.salary * self.percentage) / 100
        return bonus


# Derived Class: Manager
class Manager(Employee):
    def __init__(self, emp_id, name, salary, percentage, department, team_size, allowance):
        super().__init__(emp_id, name, salary, percentage)
        self.department = department
        self.team_size = team_size
        self.allowance = allowance

    def manager_details(self):
        print("\n--- Manager Details ---")
        print("\nID        :", self.emp_id)
        print("Name      :", self.name)
        print("Salary    :", self.salary)
        print("Department:", self.department)
        print("Team Size :", self.team_size)
        print("Allowance :", self.allowance)

    def printManager(self):   # Polymorphism (override style usage)
        bonus = self.calculate_bonus()
        total = self.salary + bonus + self.allowance
        self.manager_details()
        print("Bonus     :", bonus)
        print("\nTotal Salary:", total)


# Derived Class: Developer
class Developer(Employee):
    def __init__(self, emp_id, name, salary, percentage, project, experience):
        super().__init__(emp_id, name, salary, percentage)
        self.project = project
        self.experience = experience

    def developer_details(self):
        print("\n--- Developer Details ---")
        print("\nID        :", self.emp_id)
        print("Name      :", self.name)
        print("Salary    :", self.salary)
        print("Project   :", self.project)
        print("Experience:", self.experience, "years")

    def printDeveloper(self):
        bonus = self.calculate_bonus()
        total = self.salary + bonus
        self.developer_details()
        print("Bonus     :", bonus)
        print("\nTotal Salary:", total)


# -------- Main Program --------
print("\n\tEMPLOYEE SALARY CALCULATION...\n")
print("1. Manager\n2. Developer")
choice = int(input("Enter your choice: "))

emp_id = int(input("\nEnter Employee ID     : "))
name = input("Enter Name            : ")
salary = float(input("Enter Salary          : "))
percentage = float(input("Enter Bonus Percentage: "))

if choice == 1:
    department = input("Enter Department      : ")
    team_size = int(input("Enter Team Size       : "))
    allowance = float(input("Enter Allowance       : "))

    emp = Manager(emp_id, name, salary, percentage, department, team_size, allowance)
    emp.printManager()

elif choice == 2:
    project = input("Enter Project Name    : ")
    experience = int(input("Enter Experience (years): "))

    emp = Developer(emp_id, name, salary, percentage, project, experience)
    emp.printDeveloper()

else:
    print("Invalid choice!")
