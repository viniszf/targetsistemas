
import json

def calcular_faturamento(faturamento_diario):
    # Filtra os dias com faturamento positivo (ignora dias sem faturamento)
    dias_validos = [valor for valor in faturamento_diario if valor > 0]

    # Calcula o menor e o maior faturamento
    menor_faturamento = min(dias_validos)
    maior_faturamento = max(dias_validos)

    # Calcula a média de faturamento
    media_mensal = sum(dias_validos) / len(dias_validos)

    # Conta os dias onde o faturamento foi superior à média mensal
    dias_acima_media = sum(1 for valor in dias_validos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    # Carrega os dados de faturamento de um arquivo JSON
    try:
        with open('faturamento.json', 'r') as file:
            dados = json.load(file)
            faturamento_diario = dados['faturamento_diario']
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(f"Erro ao ler o arquivo JSON: {e}")
        return

    # Processa os dados de faturamento
    menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

    # Exibe os resultados
    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")

if __name__ == "__main__":
    main()

