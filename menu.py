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

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar Usuário')
    elif opcao_escolhida == 2:
        print('Cadastrar Vacina')
    elif opcao_escolhida == 3:
        print('Listar Vacinas')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()