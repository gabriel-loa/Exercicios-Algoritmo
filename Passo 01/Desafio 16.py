cigarros = int (input('Quantos cigarros voce fuma por dia? '))
anos = int (input('Quantos anos voce ja fumou? '))

cigarroano = int (cigarros * 365)
cigarrojafumado = int (cigarroano * anos)
perdeu = int (cigarrojafumado * 10)


diasper = perdeu / 1440

print('Voce perdeu {:.0f} dias de vida'.format(diasper))






