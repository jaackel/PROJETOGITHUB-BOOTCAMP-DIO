n = int(input('digite um numero !'))
r= n** (1/2)
print ('o dobro de {} é igual a {}'.format(n, (n*2)))
print ('o triplo de {} é igual a {}'.format(n, (n*3)))
print ('e a raiz quadrada de {}, é igual a {:.3f}'.format (n, (r)))


n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n*2}.\nO triplo é {n*3}\nA raiz quadrada é {n**(1/2):.2f}.')

#format pode ser substituído por "f", usando assim:
#Print(f'{variável} é igual à {variável}')
#Também pode-se fazer contas, como:
#Print(f'variável + 1} é igual á {variável}')
n= int(input('digite um numero !'))
print(f'o dobro de {n} é {n*1} \nO triplo de {n} é {n*2} \n E a raiz quadrada de {n} é {n**(1/2):.2f}.')
