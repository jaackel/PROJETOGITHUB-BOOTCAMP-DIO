real= float(input('digite quanto voce tem na carteira :R$'))
dolar= real / 4.73
euro= real / 5.08
print('Com o valor de R${:.2f} na carteira, voce pode comprar U$${:.2f} e EUR{:.2f} '.format(real,dolar,euro))
