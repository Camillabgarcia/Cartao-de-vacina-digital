import os

usuarios = []
vacinas = []

def exibir_nome_do_programa():
    print('Cartão de Vacina Digital : \n')

def exibir_opcoes():
    print('1.Cadastrar Usuário')
    print('2.Cadastrar Vacina')
    print('3.Listar Vacinas')
    print('4.Sair\n')

def finalizar_app():
    os.system('cls')     #limpa a tela e mostrar a seguinte mensagem:
    print('Procedimento Finalizado\n')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite um tecla para voltar ao menu principal')
    main()

def cadastrar_nova_vacina():
    os.system('cls')
    print('Cadastro de Vacina')
    nome_da_vacina = input('Digite o nome da vacina: ')
    vacinas.append(nome_da_vacina)
    lote_da_vacina =  input('Digite o lote da vacina: ')
    vacinas.append(lote_da_vacina)
    print(f'A vacina {nome_da_vacina} foi cadastrada com sucesso.')
    input('Digite um tecla para voltar ao menu principal')
    main()

def cadastrar_novo_usuario():
    os.system('cls')
    print('Cadastro do Usuário\n')
    nome_do_usuario = input('Digite o nome do usuário: ')
    usuarios.append(nome_do_usuario)
    cpf_do_usuario = input('Digite o CPF: ')
    usuarios.append(cpf_do_usuario)
    data_nascimento = input('Digite a data de nascimento: ')
    usuarios.append(data_nascimento)
    endereco_do_usuario = input('Digite o endereço: ')
    usuarios.append(endereco_do_usuario)
    print(f'O usuário {nome_do_usuario} foi cadastrado com sucesso.\n')
    input('Digite um tecla para voltar ao menu principal')
    main()

def listar_vacinas():
    os.system('cls')
    print('Lista de Vacinas\n')

    for vacina in vacinas:
        print(f'.{vacina}')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_usuario()
        elif opcao_escolhida == 2:
            cadastrar_nova_vacina()
        elif opcao_escolhida == 3:
            listar_vacinas()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()