from modulo import printdiferente

cadastro = []
while True:
    printdiferente('MENU PRINCIPAL')
    print('1-Adicionar cadastro')
    print('2-Remover cadastro')
    print('3-Exibir cadastro')
    print('4-Atualizar cadastro')
    print('5-Sair')

    try:  # verifica se o que o usuário digitou é um numero inteiro, coso não seja cai no except valor errado
        # aparece a mensagem exbindo que o numero está errado, e o continue faz com que o ele fique nesse looping
        # até digitar o um número inteiro.
        menu = int(input('digite a opção que deseja: '))
    except ValueError:
        print('O número que você digitou não está entre 1 e 5, tente novamente!')
        continue

    if menu == 1:
        while True:
            # adiciona o dicionario dentro da lista, caso ele nao queira mais adicionar um novo cadastro
            # o usuario digita n
            dic = {}
            dic['nome'] = str(input('nome: ')).strip().lower()
            dic['idade'] = int(input('idade: '))
            dic['cpf'] = str(input('cpf: '))
            cadastro.append(dic)
            print(f'cadastro foi adicionado com sucesso!')

            opcao = str(input('deseja adicionar novo cadastro?[s-sim][n-não] ')).strip().lower()[
                0]  # strip tira os espaços deixado pelo usuario
            # e o [0] e o indice da string para pegar so a primeira letra
            if opcao == 'n':
                break

    elif menu == 2:
        while True:
            # remove um cadastro de dentro da lista
            if not cadastro:
                # caso não tenha nenhuma cadastro inserido aparece essa mensagem
                print('Nenhum cadastro foi inserido')
            else:
                nome_remover = str(input(
                    'Digite o nome que deseja remover: ')).strip().lower()  # strip tira os espaços deixado pelo usuario
                removido = False  # entra direito no laço, caso o  nome seja igual o removido muda para True
                for c in cadastro:
                    if c['nome'] == nome_remover:
                        cadastro.remove(c)
                        removido = True
                        print('Cadastro foi removido com sucesso!')

                if not removido:  # verifica se o removido foi mudado de false para true caso nao seja aparece essa mensagem
                    print('O nome que você digitou não foi encontrado, tente novamente!')

            opcao = str(input('Deseja remover outro cadastro?[s-sim][n-não] ')).strip().lower()[
                0]  # strip tira os espaços deixado pelo usuario
            # e o [0] e o indice da string para pegar so a primeira letra

            if opcao == 'n':
                break

    elif menu == 3:
        # mostra os dados dentro contido na lista
        while True:
            if not cadastro:
                # caso não tenha nenhuma cadastro inserido aparece essa mensagem
                print('Nenhum cadastro foi inserido')
            else:
                for c in cadastro:
                    print(f"nome = {c['nome']}")
                    print(f"idade = {c['idade']}")
                    print(f"cpf = {c['cpf']}")
                    print('=' * 30)

            opcao = str(input('Deseja remover outro cadastro?[s-sim][n-não] ')).strip().lower()[
                0]  # strip tira os espaços deixado pelo usuario e o lower tranforma tudo um minusculo
            # e o [0] e o indice da string para pegar so a primeira letra caso o usuario digite nao
            if opcao == 'n':
                break

    elif menu == 4:
        while True:
            # edita os dados que já contem na lista
            if not cadastro:
                # caso não tenha nenhuma cadastro inserido aparece essa mensagem
                print('Nenhum cadastro foi inserido')
            else:
                nome_modificar = str(input(
                    'digite o nome que deseja modificar: ')).strip().lower()  # strip tira os espaços deixado pelo usuario e o lower tranforma tudo um minusculo
                modificado = False  # entra direito no laço, caso o  nome seja igual o removido muda para True
                for c in cadastro:
                    if nome_modificar == c['nome']:
                        modificado = True
                        printdiferente('MODIFICAR CADASTROS')
                        print('1-Modificar nome')
                        print('2-Modificar idade')
                        print('3-Modificar cpf')
                        print('4-sair')

                        # caso o nome seja igual ele ira selecionar qual dado deseja modificar

                        try:  # verifica se o que o usuario digitou é um numero inteiro
                            n = int(input('Digite a opção que deseja: '))
                        except ValueError:  # caso nao seja um numero inteiro cai aqui dentro e aparece essa mensagem
                            print('O número que você digitou não está entre 1 e 4, tente novamente!')
                            continue  # serve para o usuario ficar dentro desse looping até digitar um numero inteiro

                        if n == 1:
                            novo_nome = str(input(
                                'digite o seu novo nome: ')).strip().lower()  # strip tira os espaços deixado pelo usuario e o lower tranforma tudo um minusculo
                            c['nome'] = novo_nome

                        elif n == 2:
                            nova_idade = int(input('digite a sua idade: '))
                            c['idade'] = nova_idade

                        elif n == 3:
                            novo_cpf = str(input('digite o seu novo cpf: '))
                            c['cpf'] = novo_cpf

                        elif n == 4:
                            break

                        else:
                            print('o número que você digitou não foi encontrado, tente novamente!')

                if not modificado:  # verifica se o removido foi mudado de false para true caso nao seja aparece essa mensagem
                    print('o nome que você digitou não foi encontrado, tente novamente!')


    elif menu == 5:
        printdiferente('Muito obrigado!')
        break

    else:
        print(
            'o número que você digitou não foi encontrado, tente novamente!')  # caso o usuario nao digite um numero entre 1 e 5 ele exibi essa mensagem








