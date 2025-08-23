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