dados = (23 ,54, 46, 32, 43, 54, 32, 123, 45, 54)

m = sum(dados) / len(dados)
soma = sum([(valor - m)**2 for valor in dados])
v = soma / (len(dados) - 1)
desvio_padrao = v**0.5

print(f'Desvio padrão: {desvio_padrao:.2f}')