dados = (12, 54, 64,12, 54, 65, 34,  64, 12)

frequencias = {}

for valor in dados:
    if valor in frequencias:
        frequencias[valor]+= 1
    else:
        frequencias[valor] = 1

print(f'Frequencia de ocorrência: {max(frequencias.values())}')

#------------------------------------------------------------------------------------------------------#

dados = (23 ,54, 46, 32, 43, 54, 32, 123, 45, 54)

frequencias = {}

for valor in dados:
    if valor in frequencias:
        frequencias[valor] += 1
    else:
        frequencias[valor] = 1

print(frequencias)


