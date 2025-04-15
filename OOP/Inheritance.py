from Encapsulation import Human
class Men (Human):
    def __init__(self, name : str, age : int, beard : str):
        super().__init__(name, age)
        self.__beard = beard

    def getBeard(self):
        return self.__beard

    def setBeard(self, newBeard : str):
        self.__beard = newBeard

    def fight(self):
        print(self.getName(), " Fighting")

    def play(self):
        print(self.getName(), " Playing")

Men_1 : object = Men("Men_1", 25, "Beardo")
print(Men_1.getName(), Men_1.getAge(), Men_1.getBeard())
Men_1.fight()

Men_1.setName("New-Men_1"), Men_1.setAge(55), Men_1.setBeard("Dragon")
print(Men_1.getName(), Men_1.getAge(), Men_1.getBeard())
Men_1.fight()