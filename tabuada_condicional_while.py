def tabuada_condicional():
    numero = int(input('Digite um numero:'))
    contador = 0
    while contador <= 10:
        resultado = numero * contador
        if resultado % 3 == 0:
            print(f'{numero} x {contador} = {resultado}')
        contador += 1


tabuada_condicional()