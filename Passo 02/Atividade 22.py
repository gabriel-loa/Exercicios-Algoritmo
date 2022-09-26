print('Alistamento Militar')

nasc = int(input('Qual o ano do seu nascimento? '))
hoje = 2022

idade = hoje - nasc

if idade > 18:
    alis = idade - 18
    print('Voce ja podia ter se alistado a {} anos atras' .format(alis))

else:
    falta = 18 - idade
    print('Ainda falta {} anos para voce poder se alistar' .format(falta))