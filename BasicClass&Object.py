class Coder:
    def __init__ (self, name : str, skill : str):
        self.name = name
        self.skill = skill

dev : object = Coder("Dev", "MERN")
print((dev.name), (dev.skill))