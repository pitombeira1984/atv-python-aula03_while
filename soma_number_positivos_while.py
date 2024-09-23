def somar_numeros_positivos():
    soma = 0  # Variável para armazenar a soma dos números positivos
    
    while True:
        numero = int(input("Digite um número (negativo para sair): "))
        
        if numero < 0:
            break  # Se o número for negativo, interrompe o loop
        
        soma += numero  # Adiciona o número positivo à soma
    
    print(f"A soma dos números positivos é: {soma}")

# Chamar a função
somar_numeros_positivos()