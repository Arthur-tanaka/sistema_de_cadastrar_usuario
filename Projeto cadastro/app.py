from teste import Opcoes

sistema = Opcoes()

while True:
    print("*-"*20)
    print("1 - Cadastrar usuário\n2 - Listar usuários\n3 - Buscar usuário\n4 - Atualizar usuário\n5 - Deletar usuário\n6 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("Email: ")
        sistema.cadastrar_usuario(nome, idade, email)  

    elif opcao == "2":
        sistema.listar_usuario()

    elif opcao == "3":
        nome = input("Digite o nome para buscar: ")
        sistema.buscar_usuario(nome)

    elif opcao =="4":
        nome = input("Digite o nome do usuario que deseja atualizar: ")
        sistema.atualizar_usuario(nome)

    elif opcao == "5":
        nome = input("Digite o nome da pessoa que deseja deletar: ")
        sistema.deletar_usuario(nome)    
    
    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
