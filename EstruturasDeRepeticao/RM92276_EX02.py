print('GESTÃO DE GASTOS FINANCEIROS')

#entrada do número de transações
transacoes = int(input('Qual o número de transações realizadas ao longo do dia de hoje? '))

#variável que acumula o total que foi gasto
valor = 0

#entrada
for gastos in range(1, transacoes + 1):
    custo = float(input(f'Quanto foi gasto na transação {gastos} em R$? '))
    valor = valor + custo

#resultado final
print(f'Foram feitas {transacoes} transações, o total foi de R$ {valor} e a média foi R$ {valor/transacoes:.2f}')