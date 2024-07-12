dados = (23 ,54, 46, 32, 43, 54, 32, 123, 45, 54)

media = sum(dados) / len(dados)

soma = 0

for i in dados:
    soma += (i - media)**2

variancia_amostral = soma / (len(dados) - 1)
variancia_populacional = soma / len(dados)

print(f'Variancia amostral: {variancia_amostral:.2f}')

print(f'Variancia populacional: {variancia_populacional:.2f}')
