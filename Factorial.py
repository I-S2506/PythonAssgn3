def fac(n):
    if n < 2:
        return 1
    return n * fac(n - 1)

num = int(input("Enter a number: "))

result = fac(num)
print("Factorial of", num, "is:", result)