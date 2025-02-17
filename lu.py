# Nome da Disciplina: Programação
# Nome da Turma: 1A
# Nomes dos Alunos:luzia gaby


def cadastrar_convidado(convidados):
    nome = input("Digite o nome do convidado: ")
    convidados.append(nome)
    print(f"{nome} foi cadastrado com sucesso!")

def consultar_convidados(convidados):
    if not convidados:
        print("Não há convidados cadastrados.")
    else:
        print("Convidados:")
        for i, convidado in enumerate(convidados):
            print(f"{i + 1}. {convidado}")

def atualizar_convidado(convidados):
    consultar_convidados(convidados)
    try:
        indice = int(input("Digite o número do convidado que deseja atualizar: ")) - 1
        if 0 <= indice < len(convidados):
            novo_nome = input("Digite o novo nome do convidado: ")
            convidados[indice] = novo_nome
            print("Convidado atualizado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def apagar_convidado(convidados):
    consultar_convidados(convidados)
    try:
        indice = int(input("Digite o número do convidado que deseja apagar: ")) - 1
        if 0 <= indice < len(convidados):
            removido = convidados.pop(indice)
            print(f"{removido} foi removido com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def menu():
    convidados = []
    while True:
        print("\nMenu de Operações:")
        print("1. Cadastrar Convidado")
        print("2. Consultar Convidados")
        print("3. Atualizar Convidado")
        print("4. Apagar Convidado")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_convidado(convidados)
        elif opcao == '2':
            consultar_convidados(convidados)
        elif opcao == '3':
            atualizar_convidado(convidados)
        elif opcao == '4':
            apagar_convidado(convidados)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()