def calcular_percentual_faturamento(faturamento_por_estado):
    # Calcula o faturamento total
    faturamento_total = sum(faturamento_por_estado.values())

    # Calcula o percentual de cada estado
    percentual_por_estado = {
        estado: (valor / faturamento_total) * 100
        for estado, valor in faturamento_por_estado.items()
    }

    return percentual_por_estado

def main():
    # Dados de faturamento por estado
    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    # Calcula percentuais de faturamento
    percentuais = calcular_percentual_faturamento(faturamento_por_estado)

    # Exibe os percentuais de representação de cada estado
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
