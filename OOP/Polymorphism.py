from Encapsulation import Human
from Inheritance import Men

Men_P1: object = Human("Men_P1", 25)
print(Men_P1.getName(), Men_P1.getAge())
Men_P1.run()
Men_P1.play()

Men_P2 : object = Men("Men_P2", 25, "Beardo")
print(Men_P2.getName(), Men_P2.getAge(), Men_P2.getBeard())
Men_P2.fight()
Men_P2.run()
Men_P2.play()