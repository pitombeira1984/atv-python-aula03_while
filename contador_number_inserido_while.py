def contar_numero_inserido():
    contador = 1
    limite = int(input('Digite o limite:'))
    while contador <= limite:
        if contador % 2 != 0:
            print(contador)
        contador += 1

# Chamar a função
contar_numero_inserido()