def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('Tienes $' + dolares + ' dolares')

menu = """
Bienvenida al conversor de monedas

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige ina opcion:
"""

opcion = input(menu)

if opcion == '1':
    dolares = conversor('mexicanos',19.87)

elif opcion == '2':
    dolares = conversor('colombianos',3875)

elif opcion == '3':
    dolares = conversor('argentinos',65)
    
else:
    print('Ingresa una opcion disponible')

