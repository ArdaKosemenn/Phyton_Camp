class Person:
    def __init__(self,name,lastName):
        self.name=name
        self.lastName=lastName
    
    
müsteri1=Person("Engin", "Demiroğ")
müsteri2=Person("Arda", "Kösemen")
müsteri3=Person("Ahmet", "Demiroğ")

print(müsteri2.name,müsteri2.lastName)