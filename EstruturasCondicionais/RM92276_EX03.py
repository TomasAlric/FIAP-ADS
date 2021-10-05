votoSegunda = int(input('Qual a quantidade de votos na segunda? '))
votoTerca = int(input('Qual a quantidade de votos na terça? '))
votoQuarta = int(input('Qual a quantidade de votos na quarta? '))
votoQuinta = int(input('Qual a quantidade de votos na quinta? '))
votoSexta = int(input('Qual a quantidade de votos sexta? '))

if votoSegunda > votoTerca and votoSegunda > votoQuarta and votoSegunda > votoQuinta and votoSegunda > votoSexta:
    print('Segunda-feira venceu!')
elif votoTerca > votoSegunda and votoTerca > votoQuarta and votoTerca > votoQuinta and votoTerca > votoSexta:
    print('Terça-feira venceu!')
elif votoQuarta > votoSegunda and votoQuarta > votoTerca and votoQuarta > votoQuinta and votoQuarta > votoSexta:
    print('Quarta-feira venceu!')
elif votoQuinta > votoSegunda and votoQuinta > votoQuarta and votoQuinta > votoTerca and votoQuinta > votoSexta:
    print('Quinta-feira venceu!')
elif votoSexta > votoSegunda and votoSexta > votoQuarta and votoSexta > votoQuinta and votoSexta > votoTerca:
    print('Sexta-feira venceu!')
else:
    print('Empatou, será necessário outra votação')

