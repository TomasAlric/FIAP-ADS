peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))

imc = peso / (altura ** 2)

print('O seu IMC é de {:.2f}'.format(imc))

if 18.50 <= imc <= 24.99:
    print('Você está na categoria Peso ideal')

elif 17.00 <= imc <= 18.49:
    print('Você está na categoria Baixo peso Grau I')

elif 16.00 <= imc <= 16.99:
    print('Você está na categoria Baixo peso Grau II')

elif imc < 16.00:
    print('Você está na categoria Baixo peso Grau III')

elif 25.00 <= imc <= 29.99:
    print('Você está na categoria Sobrepeso')

elif 30.00 <= imc <= 34.99:
    print('Você está na categoria Obesidade Grau I')

elif 35.00 <= imc <= 39.99:
    print('Você está na categoria Obesidade Grau II')

elif imc >= 40.00:
    print('Você está na categoria Obesidade Grau III')
