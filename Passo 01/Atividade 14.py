print('Bem vindo a Concessionaria')

km =  float (input('Quantos Kms vc fez? '))
dias = int (input('Quantos dias voce ficou com o carro? '))

kmvalor = float (0.20) * km
diasvalor = 90 * dias 
valor = float (kmvalor + diasvalor)

print('O valor do aluguel e de: ' , valor)
