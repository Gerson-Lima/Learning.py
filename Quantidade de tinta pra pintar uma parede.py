b = (float(input('Qual a largura, em metros, da parede que deseja pintar?')))
h = (float(input('Qual a altura, em metros, da parede que deseja pintar?')))
a = (b*h)
print('A área dessa parede é: {}m².'.format(a))
#Cada litro de tinta pinta uma área de 2m² = (2**2m)
qtdtinta = (a/2)
print('A quantidade de tinta necessária para pintar essa parede é de {} litros de tinta.'.format(qtdtinta))
