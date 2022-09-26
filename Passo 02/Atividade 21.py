print('Bem-vindo ao descubridor de anos bisssextos!!!')

ano = int (input('Digite algum ano: '))

bis = ano % 4

if bis == 0:
    print('Esse é um ano bissexto')

else:
    print('Esse não é um ano bissexto')