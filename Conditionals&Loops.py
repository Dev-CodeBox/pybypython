n : int = (int)(input("Enter The Iteraion You Want -> "))
for i in range(0, n, +1):
    name : str = input("Enter Any String -> ")
    if(name.isalpha() == 1):
        print(name, " -> Is String")
    elif(name.isnumeric() == 1):
        print(name, " -> Is Integer")
    else:
        print(None)

