def is_fibonacci_number(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True

    a, b = 0, 1
    while b < n:
        a, b = b, a + b

    return b == n

def main():
    # Número a ser verificado
    numero = int(input("Informe um número: "))

    if is_fibonacci_number(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()

