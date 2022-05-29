def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
# first consition not met so factorial is called 3 times
# with decremented value of n and added onto the callstack

# once n == 1 the values are returned to the previous stack calls until it is fed to the original call for factiorial(4)
