nome = str(input('Qual o seu nome? '))

nota1 = float(input('Qual a sua nota no primeiro semetre? '))
nota2 = float(input('Qual a sua nota no segundo semetre? '))

media = (nota1 + nota2) / 2

if media > 7:
    print('Parebens {}, você foi aprovado' .format(nome))

else:
    print('Lamento {}, você não foi aprovado' .format(nome))