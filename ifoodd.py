import os

 

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},

                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},

                {'nome':'Canti', 'categoria':'Italiano', 'ativo':False}]

 

def exibir_nome_programa():

    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗

██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝

╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░

░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗

██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝

╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

 

def exibir_opcoes():

    print('1. Cadastrar restaurante')

    print('2. Listar restaurante')

    print('3. Ativar restaurante')

    print('4. Sair\n')

 

def finalizar_app():

    exibir_sub('Finalizando o app\n')

 

def voltar_ao_menu_principal():

    print('-------------------------------------')

    input('Digite uma tecla para voltar ao menu:\n')

    main()

 

def exibir_sub(texto):

    os.system('cls')

    linha = '*'*(len(texto))

    print(linha)

    print(texto)

    print()

 

def opcao_invalida():

    print('-------------------')

    print('Opcao Invalida')

    voltar_ao_menu_principal()

 

def cadastrar_novo_restaurante():

    exibir_sub('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante:')

    categoria = input('Digite a categoria do restaurante:')

    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com Sucesso!\n')

    voltar_ao_menu_principal()

 

def listar_restaurante():

    exibir_sub('Listando os restaurantes:\n')

    for restaurante in restaurantes:

        nome_restaurante = restaurante['nome']

        categoria = restaurante['categoria']

        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f' - {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_sub('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')


    voltar_ao_menu_principal()




def escolher_opcoes():  

    try:

        opcao_escolhida = int (input('Digite uma opcao: '))

        if opcao_escolhida == 1:

            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:

            listar_restaurante()

        elif opcao_escolhida == 3:

            alternar_estado_restaurante()

        elif opcao_escolhida == 4:

            print('Sair')

        else :

            opcao_invalida()

    except:

        opcao_invalida()

   

def main():

    os.system('cls')

    exibir_nome_programa()

    exibir_opcoes()

    escolher_opcoes()

 

if __name__ == '__main__':

    main()

 