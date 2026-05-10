#FINDING TOTAL MARKS
# Base Class
class Student:
    def __init__(self, name, roll_no, test_mark):
        self.name = name
        self.roll_no = roll_no
        self.test_mark = test_mark

    def total_marks(self):
        return self.test_mark

    def display(self):
        print("\n--- Student Details ---")
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)
        print("Test Marks:", self.test_mark)
        print("Total Marks:", self.total_marks())


# Derived Class: Literary Student
class Literary_Student(Student):
    def __init__(self, name, roll_no, test_mark, literary_marks):
        super().__init__(name, roll_no, test_mark)
        self.literary_marks = literary_marks

    def total_marks(self):   # Polymorphism
        return self.test_mark + self.literary_marks

    def display(self):
        print("\n--- Literary Student ---")
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)
        print("Test Marks:", self.test_mark)
        print("Literary Marks:", self.literary_marks)
        print("Total Marks:", self.total_marks())


# Derived Class: Sports Student
class Sports_Student(Student):
    def __init__(self, name, roll_no, test_mark, sports_marks):
        super().__init__(name, roll_no, test_mark)
        self.sports_marks = sports_marks

    def total_marks(self):   # Polymorphism
        return self.test_mark + self.sports_marks

    def display(self):
        print("\n--- Sports Student ---")
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)
        print("Test Marks:", self.test_mark)
        print("Sports Marks:", self.sports_marks)
        print("Total Marks:", self.total_marks())


# Derived Class: Literary + Sports Student
class Lit_Sport_Student(Literary_Student, Sports_Student):
    def __init__(self, name, roll_no, test_mark, literary_marks, sports_marks):
        Student.__init__(self, name, roll_no, test_mark)
        self.literary_marks = literary_marks
        self.sports_marks = sports_marks

    def total_marks(self):   # Polymorphism
        return self.test_mark + self.literary_marks + self.sports_marks

    def display(self):
        print("\n--- Literary & Sports Student ---")
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)
        print("Test Marks:", self.test_mark)
        print("Literary Marks:", self.literary_marks)
        print("Sports Marks:", self.sports_marks)
        print("Total Marks:", self.total_marks())


# -------- Main Program --------
print("\n\tFINDING TOTAL MARKS...\n")
print("1. Student\n2. Literary Student\n3. Sports Student\n4. Literary & Sports Student")
choice = int(input("Enter your choice: "))

name = input("\nEnter Name: ")
roll_no = int(input("Enter Roll No: "))
test_mark = float(input("Enter Test Marks: "))

if choice == 1:
    s = Student(name, roll_no, test_mark)
    s.display()

elif choice == 2:
    literary_marks = float(input("Enter Literary Marks: "))
    s = Literary_Student(name, roll_no, test_mark, literary_marks)
    s.display()

elif choice == 3:
    sports_marks = float(input("Enter Sports Marks: "))
    s = Sports_Student(name, roll_no, test_mark, sports_marks)
    s.display()

elif choice == 4:
    literary_marks = float(input("Enter Literary Marks: "))
    sports_marks = float(input("Enter Sports Marks: "))
    s = Lit_Sport_Student(name, roll_no, test_mark, literary_marks, sports_marks)
    s.display()

else:
    print("Invalid choice!")
