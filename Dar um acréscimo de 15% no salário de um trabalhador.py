s = (float(input('Saber novo salário com 15% de aumento:')))
aum = (s*(15/100))
print('Seu novo salário com acréscimo de 15%, é R${} reais.'.format(aum+s)) 
#Há soma do valor inicial após o cálculo do aumento!
#Diferente da aula 012, fiz a diferença no .format, com a adição do aumento.