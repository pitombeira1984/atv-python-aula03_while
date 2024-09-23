def senha():
    senha = ""
    while senha != '1234':
        senha = input('Digite a senha: ')
        if senha == '1234':
            print('Acesso Concedido')
        else:
            print('Senha incorreta, tente novamente.')

senha()  

