def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Escriba el mes que desea conocer: "))
print(f'En el mes número {n} habrán {fibonacci(n)} conejos')
