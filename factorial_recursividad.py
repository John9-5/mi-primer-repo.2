def factorial(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n * factorial(n-1)
    
numero = int(input("Ingrese el que desea hallar su factorial:"))
print(factorial(numero))