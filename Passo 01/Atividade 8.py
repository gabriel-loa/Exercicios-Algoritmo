metros = float (input('Digite um valor em metros '))
cm = float (metros * 100)
km = float (metros / 1000)

print('O valor em kilometros é igual {:.3f} km' .format(km))
print('O valor em milimetros é igual {:.0f} mm' .format(cm))