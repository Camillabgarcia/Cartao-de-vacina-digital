class CartaoDeVacina:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.data_nascimento = None
        self.endereco = None
        self.vacinas = []

    def adicionar_usuario(self):
        print('* Cadastro do Usuário *')
        self.nome = input('Nome: ')
        self.cpf = input('Cpf: ')
        self.data_nascimento = input('Data de Nascimento: ')
        self.endereco = input('Endereço: ')

    def cadastrar_vacina(self):
        if not self.nome:
            print('É necessário fazer o cadastro do usuário primeiro.')
            return

        print('Cadastro da Vacina')
        nome_vacina = input('Nome da Vacina: ')
        lote_vacina = input('Lote da Vacina: ')
        doses_totais = int(input('Quantidade total de doses: '))

        vacina = {
            'nome': nome_vacina,
            'lote': lote_vacina,
            'doses_totais': doses_totais,
            'doses_aplicadas': 0
        }

        self.vacinas.append(vacina)

    def aplicar_dose(self):
        if not self.nome:
            print('É necessário fazer o cadastro do usuário primeiro.')
            return
        
        nome_vacina = input('Digite o nome da vacina: ')
        vacina_encontrada = False

        for vacina in self.vacinas:
            if vacina['nome'] == nome_vacina:
                if vacina['doses_aplicadas'] < vacina['doses_totais']:
                    vacina['doses_aplicadas'] += 1
                    print(f'Foi aplicado com sucesso a dose da vacina: {nome_vacina}')
                else:
                    print(f'Já foram aplicadas todas as doses da vacina : {nome_vacina}')
                break
        if not vacina_encontrada:
            print(f'A vacina {nome_vacina}, não está cadastrada no cartão.')

    def exibir_cartao(self):
        if not self.nome:
            print('É necessário fazer o cadastro do usuário primeiro.')
            return

        else:
            print('Informações de Cartão de Vacinação Digital')
            print(f'Nome: {self.nome}')
            print(f'Cpf: {self.cpf}')
            print(f'Data de Nascimento: {self.data_nascimento}')
            print(f'Endereço: {self.endereco}')
            print()
            print('Vacinas\n')
        for vacina in self.vacinas:
            print(f'Nome: {vacina['nome']}')
            print(f'Lote: {vacina['lote']}')
            print(f'Doses totais: {vacina['doses_totais']}')
            print(f'Doses aplicadas: {vacina['doses_aplicadas']}')

def main():
    cartao_vacina = CartaoDeVacina()

    while True:
        print('Cartão de Vacina Digital : \n')
        print('1.Cadastrar Usuário')
        print('2.Cadastrar Vacina')
        print('3.Doses ')
        print('4.Exibir Cartão de Vacinação')
        print('5.Sair\n')

        opcao = input('Escolha a opção: ')
        print()

        if opcao == '1':
            cartao_vacina.adicionar_usuario()
        elif opcao == '2':
            cartao_vacina.cadastrar_vacina()
        elif opcao == '3':
            cartao_vacina.aplicar_dose()
        elif opcao == '4':
            cartao_vacina.exibir_cartao()
        elif opcao == '5':
            break
        else:
            print('Opção inválida, retorne ao menu principal.')

if __name__ == '__main__':
    main()



