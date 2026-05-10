class department:
    def getdeptdetails(self):
        print("\nENTER DEPARTMENT DETAILS...")
        self.did = input("Enter Deparment ID: ")
        self.dname = input("Enter Department: ")
        
class course(department):
    def getcourse(self):
        print("\nENTER COURSE DETAILS...")
        self.n = int(input("Enter number of courses: "))
        self.c = []
        for i in range(self.n):
            print()
            a = input(f"Enter course name {i+1}: ")
            b = int(input("Enter course code: "))
            c = input("Enter duration: ")
            
            d = [a,b,c]
            self.c.append(d)
            
class student(course):
    def getdetails(self):
        print("\nENTER STUDENT DETAILS...")
        self.roll = input("Enter roll number: ")
        self.sname = input("Enter Student name: ")
        print()
        for i in range(self.n):
            m = float(input(f"Enter mark for {self.c[i][0]}: "))
            self.c[i].append(m)
                
    def printstudent(self):
        print()
        print(f"{'STUDENT DETAILS':^65}")
        print()
        print("-"*65)
        print(f"{'Department name ':<20}:{self.dname:<15}{'Student name ':<20}:{self.sname:<10}")
        print(f"{'Department ID ':<20}:{self.did:<15}{'Student roll no ':<20}:{self.roll:<10}")
        print("-"*65)
        print(f"{'Course code':<20}{'Course name':<20}{'Marks':<10}{'Duration':<15}")
        print()
        for r in self.c:
            print(f"{r[1]:<20}{r[0]:<20}{r[3]:<10}{r[2]:<15}")
    
        
s1 = student()
s1.getdeptdetails()
s1.getcourse()
s1.getdetails()
s1.printstudent()
