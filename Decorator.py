def wheel(func):
    def wrapper():
        print("Added Wheel To Machine")
        return func()
    return wrapper

@wheel
def machine():
    print("Now My Machine Is Ready To Run")

machine()