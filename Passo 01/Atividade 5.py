bi1 = float (input('Qual a sua nota no primeiro bimestre '))
bi2 = float (input('Qual a sua nota no segundo bimestre '))
bi3 = float (input('Qual a sua nota no terceiro bimestre '))
bi4 = float (input('Qual a sua nota no quarto bimestre '))

media = (bi1 + bi2 + bi3 + bi4) / 4

'''if media >= 7:
    print('{:.2f} APROVADO' .format(media))
else:
    print('{:.2f} REPROVADO' .format(media))
    '''


print('A media da sua nota: {:.1f}'.format(media))