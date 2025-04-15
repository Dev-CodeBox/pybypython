num : int = 0
def sum(num):
    arr = [1, 2, 3, 4, 5]
    def sumFun(num):
        for i in range(0, len(arr), +1):
            num += arr[i]
        return num
    return sumFun(num)

print(sum(num))