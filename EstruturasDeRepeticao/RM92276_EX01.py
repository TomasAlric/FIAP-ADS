print('CONTADOR DE CALORIAS')

#entrada de alimentos
alimentos = int(input('Quantos alimentos foram ingeridos no dia de hoje? '))

#variável que acumula o número de calorias
calorias = 0

#loop para armazenar calorias
for ali in range(1, alimentos + 1):
    ncalorias = float(input(f'Quantas calorias foram consumidas no alimento {ali}? '))

    calorias = calorias + ncalorias

#resultado final
print(f'No dia de hoje foram consumidos {alimentos} alimentos e um total de {calorias} calorias')