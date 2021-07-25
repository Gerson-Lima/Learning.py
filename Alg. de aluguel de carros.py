km = (float(input('Informe a quantidade de quilômetros percorridos desde o aluguel?')))
dias = (int(input('Informe a quantidade de dias desde o aluguel do automóvel?')))
pago = (km*0.15) + (dias*60)
print('O total a pagar é de R${:.2f}'.format(pago))