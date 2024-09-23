def tabuada():
    numero = int(input('Digite um numero:'))
    contador = 0
    while contador <= 10:
        resultado = numero * contador
        print(f'{numero} x {contador} = {resultado}')
        contador += 1


tabuada()    
    