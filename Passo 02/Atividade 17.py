vel = float(input('Qual a velocidade do seu carro? '))
multa = 5 * (vel - 80)

if vel > 80:
    print('Você esta multado!!!')
    print('A sua multa é de {} reais' .format(multa))

else:
    print('Obrigado por não ultrapassar o limite de velocidade ❤️')

