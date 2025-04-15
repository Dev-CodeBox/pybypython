class Human:
    def __init__(self, name : str, age : int):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self, newName : str):
         self.__name = newName

    def getAge(self):
        return self.__age

    def setAge(self, currentAge : int):
         self.__age = currentAge

    def run(self):
        print(self.__name, " Running")

    def play(self):
        print(self.__name, " Playing")

Human_1 : object = Human("Human_1", 25);
print(Human_1.getName(), Human_1.getAge())
Human_1.run()

Human_1.setName("New-Human_1"), Human_1.setAge(55)
print(Human_1.getName(), Human_1.getAge())
Human_1.run()