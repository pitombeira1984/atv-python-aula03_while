def SomaNumerosDigitados():
  try:
    soma = 0
    while True:
      numero = int(input("Digite um número (ou 0 para sair): "))
      if numero == 0:
        break
      soma += numero
    print("A soma dos números digitados é:", soma)
  except ValueError:
    print("Você digitou um valor inválido. Por favor, digite um número.")
SomaNumerosDigitados()

