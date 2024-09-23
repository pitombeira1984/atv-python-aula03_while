def media_notas():
    contador = 0
    soma = 0.0
    
    while True:
        nota = float(input(f'Digite a {contador + 1}ª nota (ou -1 para sair): '))
        
        if nota == -1:
            break
        
        soma += nota 
        contador += 1
    
    if contador > 0:
        media = soma / contador
        print(f'A média das notas é: {media:.2f}')
    else:
        print("Nenhuma nota válida foi inserida.")

media_notas()

