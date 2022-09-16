codigoUsuario = int(input("Informe o código de usuário: "))
senha = int(input("Digite a senha: "))

if codigoUsuario == 1234 and senha == 9999:
    print("Acesso liberado")

else:
    print("A senha e/ou código estão errados")
