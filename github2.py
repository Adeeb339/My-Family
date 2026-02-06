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
