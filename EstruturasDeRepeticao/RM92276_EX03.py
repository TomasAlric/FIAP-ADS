print('ALGORITMO DA SORTE DE FIBONACCI')

#entrada do número que será validado
numero = int(input('Digite um valor número inteiro: '))

a = 0
b = 1
c = a + b

#loop que realiza a soma dos números
while c < numero:
    a = b
    b = c
    c = a + b

#condicionais
if numero <= 0:
    print('Ação inválida, digite um número inteiro')

elif numero == 1:
    print('Ação bem sucedida! O número encontra-se na sequência de Fibonacci')

elif numero == 2:
    print('Ação bem sucedida! O número encontra-se na sequência de Fibonacci')

elif c == numero:
    print('Ação bem sucedida! O número encontra-se na sequência de Fibonacci')

elif c > numero:
    print('Ação mal sucedida! O número NÂO se encontra na sequência de Fibonacci')