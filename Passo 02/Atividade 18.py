nas = int(input('Qual ano em que você nasceu? '))
hoje = 2022

idade = hoje - nas

if idade > 18:
    print('Você pode votar')

else:
    print('Você não pode votar')