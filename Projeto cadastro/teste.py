usuarios = {}

class Opcoes:

    # Cadastrar Usuário
    def cadastrar_usuario(self, nome, idade, email):
        if nome in usuarios:
            print("Erro: usuário já cadastrado!")
        else:
            usuarios[nome] = {
                "idade": idade,
                "email": email   
            }
            print("Usuário cadastrado com sucesso!")

    # Listar Usuários
    def listar_usuario(self):
        if not usuarios: 
            print("Nenhum usuário cadastrado")
        else:
            for chave in usuarios:
                print("Nome:", chave, "- Idade:", usuarios[chave]["idade"], "- Email:", usuarios[chave]["email"])

    # Buscar Usuário
    def buscar_usuario(self, nome):
        if nome not in usuarios:
            print("Usuário não encontrado!")
        else:
            print("Dados do usuário:", usuarios[nome])

    # Atualizar usuários
    def atualizar_usuario(self, nome):
        if nome not in usuarios:
            print("Não foi possível atualizar o usuário, ele não existe.")
            return

        print("Se não quiser mudar algum dado, apenas aperte ENTER.")
        novo_nome = input("Digite o novo nome: ")
        nova_idade = input("Digite a nova idade: ")
        novo_email = input("Digite o novo email: ")

        if not novo_nome.strip():
            novo_nome = nome
        if not nova_idade.strip():
            nova_idade = usuarios[nome]["idade"]
        if not novo_email.strip():
            novo_email = usuarios[nome]["email"]

        if novo_nome != nome:
            usuarios[novo_nome] = {"idade": nova_idade, "email": novo_email}
            del usuarios[nome]
        else:
            usuarios[nome]["idade"] = nova_idade
            usuarios[nome]["email"] = novo_email

        print("Usuário atualizado com sucesso!")


    # Deletar Usuário
    def deletar_usuario(self, nome):
        if nome in usuarios:
            del usuarios[nome]
            print(f"Usuario: {nome} deletado com sucesso!")
        else:
            print("Usuário não cadastrado / não encontrado")
