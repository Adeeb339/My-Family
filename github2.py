class Person:
    def __init__(self, name, gender, hobbies, child=None):
        self.name=name
        self.gender=gender
        self.hobbies=hobbies
        self.child=child
        

    def show_info(self):
        print(f"{self.name}'s gender: {self.gender} | {self.name}'s hobbies: {self.hobbies} | {self.name}'s child: {self.child}")
class Pat_Grand_Parent(Person):
    pass
    
class Mat_Grand_Parent(Person):
    pass

class Father(Pat_Grand_Parent):
    pass

class Mother(Mat_Grand_Parent):
    pass

class Child(Father,Mother):
   pass

# Objects

child1=Child("Adeeb", "Male", "Football, Cricket")
father=Father("Rubayet", "Male", "Fishing, Reading", "Adeeb")
mother=Mother("Salma", "Female", "Cooking, Baking", "Adeeb")

mat_grand_parent1=Mat_Grand_Parent("Ayesha", "Female", "Reading", "Salma")
mat_grand_parent2=Mat_Grand_Parent("Abdullah", "Male", "Reading", "Salma")

pat_grand_parent1=Pat_Grand_Parent("Tahura", "Female", "Gardening, Reading", "Rubayet")
pat_grand_parent2=Pat_Grand_Parent("Muhammad", "Male", "Reading", "Rubayet")

person_selector= int(input("Please enter any number between: 1, 2, 3, 4, 5, 6, 7 or 8  to see the information of any family member: "))

