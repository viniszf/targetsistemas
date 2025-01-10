def inverter_string(s):
    # Inicializa uma string vazia para o resultado invertido
    string_invertida = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        # Adiciona cada caractere à string invertida
        string_invertida += s[i]
    
    return string_invertida

def main():
    # String de entrada (pode ser alterada ou recebida via input)
    string_original = input("Informe a string a ser invertida: ")

    # Inverte a string
    string_invertida = inverter_string(string_original)

    # Exibe a string invertida
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
