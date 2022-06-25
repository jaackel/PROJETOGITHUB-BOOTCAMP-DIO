medida= float(input('uma distancia em metros : '))
cm= (medida) / 100
mm= (medida) / 1000
km= medida * 1000
dam= medida * 100
print('A distancia de {}, é igual a {}cm e a {}mm'.format(medida,cm,mm))
print('E o valor da metragem de {} , é igual a {}km e a {}dam'.format(medida, km,dam ))

