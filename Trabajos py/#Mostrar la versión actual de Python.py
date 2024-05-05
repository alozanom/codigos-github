#Mostrar la versión actual de Python

import sys
print(sys.version)

print(sys.version_info)


print('pyton', 'es', 'tremendo', sep='-')

import datetime

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

print()

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))

#Solicitar el valor del radio de un circulo para calcular su área

from math import pi

r = float(input('Escriba el radio del circulo: '))

area = pi * r ** 2

print ('El área del circulo es {}'.format(area))