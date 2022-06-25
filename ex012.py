prec= float (input('Qual é o preço do produto ?:'))
desc= prec - (prec*5/100)
print('o preço do produto que custava {:.2f}, com o desconto de 5% agora custa {:.2f} '.format(prec,desc,))