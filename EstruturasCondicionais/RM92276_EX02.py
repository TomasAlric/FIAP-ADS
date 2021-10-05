assinatura = str(input('Qual seu tipo de assinatura? '))
faturamentoAnual = float(input('Quanto foi seu faturamento anual? '))

if assinatura == 'basic':
    bonus = faturamentoAnual * 0.3
    print('O seu bônus foi de {}'.format(bonus))

elif assinatura == 'silver':
    bonus = faturamentoAnual * 0.2
    print('O seu bônus foi de {}'.format(bonus))

elif assinatura == 'gold':
    bonus = faturamentoAnual * 0.1
    print('O seu bônus foi de {}'.format(bonus))

elif assinatura == 'platinum':
    bonus = faturamentoAnual * 0.05
    print('O seu bônus foi de {}'.format(bonus))