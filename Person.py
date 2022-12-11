class Person:
   def __init__(self, age, name, ismale, height, weight):
    self.age = age
    self.name = name
    self.ismale = ismale
    self.height = height
    self.weight = weight
    self.bmi = (703*self.weight)/(self.height*self.height)

def HealthRec(p):
 if p.bmi >= 26:
  print("Hi" + p.name + ", we recommend going on a diet and exercising.")
 else:
  print("Hi " + p.name + ", you are within the healthy range.")

Fei = Person(49, "Fei", True, 70.0, 163.0)
SumoWrestler = Person(37, "Hakuho Sho", True, 76.0, 340)

HealthRec(SumoWrestler)
