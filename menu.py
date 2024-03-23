import os

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


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('Cadastrar Usuário')
        elif opcao_escolhida == 2:
            print('Cadastrar Vacina')
        elif opcao_escolhida == 3:
            print('Listar Vacinas')
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