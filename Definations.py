num : int = (int)(input("Enter The Value For num -> "))
def printSqure(num : int):
    for i in range(0, 1, +1):
        num *= num
    return num

square = printSqure(num)
print(square)