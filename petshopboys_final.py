# FUNÇÃO VALOR DO PRODUTOS:

def val_prod(s, n):
    if s == 'ração' or s == 'R':
        return 199.90 * n
    elif s == 'ração_premium' or s == 'RP':
        return 259.90 * n
    elif s == 'brinquedo' or s == 'BR':
        return 39.90 * n
    elif s == 'remédio' or s == 'RM':
        return 59.90 * n
    return 'Erro'


# FUNÇÃO VALOR SERVIÇOS:

def val_serv(s, n):
    if s == 'tosa' or s == 'T':
        return 59.90 * n
    elif s == 'banho' or s == 'B':
        return 49.90 * n
    elif s == 'passeio' or s == 'P':
        return 39.90 * n
    elif s == 'hotel' or s == 'H':
        return 119.90 * n
    return 'Erro'


# FUNÇÃO EXIBIR LISTA DE PRODUTOS:

def exibir_lista(l):
    for e in l:
        qnt = e[0]
        prod = e[1]
        val = e[2]

        if e[0] > 1:
            print(f'{qnt} unidades de {prod} = R$ {val:.2f}')
        else:
            print(f'{qnt} unidade de {prod} = R$ {val:.2f}')


# FUNÇÃO TROCO:

def troco(numero):
    cinquenta = int(numero / 50)
    numero = numero - (cinquenta * 50)

    vinte = int(numero / 20)
    numero = numero - (vinte * 20)

    dez = int(numero / 10)
    numero = numero - (dez * 10)

    cinco = int(numero / 5)
    numero = numero - (cinco * 5)

    dois = int(numero / 2)
    numero = numero - (dois * 2)

    um = numero

    print('Notas R$ 50,00 = ', cinquenta)
    print('Notas R$ 20,00 = ', vinte)
    print('Notas R$ 10,00 = ', dez)
    print('Notas R$  5,00 = ', cinco)
    print('Notas R$  2,00 = ', dois)
    print('Notas R$  1,00 = ', um)


# FUNÇÃO PARA IDENTIFICAR O ITEM A SER REMOVIDO:

def identifica(l, s):
    i = 0
    for e in l:
        if e[1] == s:
            return i
        else:
            i += 1


# FUNÇÃO ADEQUAÇÃO LETRA EM PALAVRA

def adeq(l, s):
    for e in l:
        if e[1] == s:
            return e[0]
    else:
        return s


# FUNÇÃO ENCERRAMENTO DO CÓDIGO:

def bye(l, carrinho):
    print(f'\n\n\nSucesso, {name}! Sua compra já foi validada! :D')
    print('\n\nSegue sua notinha:')
    print('-' * 35)
    print(' ' * 13 + 'NOTA FISCAL\n')
    exibir_lista(l)
    print('-' * 35)
    print(f'Valor total: R$ {carrinho:.2f}')
    print('-' * 35)
    print(f'\nA PetShopBoys agradece pela sua compra!\n\nVolte sempre, {name}!')
    print(
        f'\n\nPs.: Ei, não fui eu quem te disse, mas tá aqui um cupom de desconto para você compartilhar com a galera: {name}TemOPetMaisLindo\n\n')


# FUNÇÃO MÉTODOS DE PAGAMENTO:

def pagamento(s, tot, l):
    if s == 'dinheiro' or s == 'DR':
        print(f'\nValor da compra: R$ {tot:.2f}')
        val = float(input(f'\nDeseja troco para quanto?\n> '))
        while val < tot:
            val = float(input(f'\nValor inválido. Deseja troco para quanto?\n> '))
        val_troco = (val - tot) // 1
        print(f'\nSeu troco será de: R$ {val_troco:.2f}\n')
        troco(val_troco)
        bye(l, tot)

    elif s == 'cartão_de_crédito' or s == 'CC':
        print(f'\nValor da compra: R$ {tot:.2f}\n')
        qnt_parc = int(input(f'Gostaria de parcelar em quantas vezes?\nPodemos fazer em até 5 vezes sem juros!\n> '))

        while qnt_parc > 5 or qnt_parc < 1:
            qnt_parc = int(input('Ops! Nº de parcelas inválido. Tenta outro:\n> '))
        parM = tot / qnt_parc
        print(f'\nValor da parcela: R$ {parM:.2f}')
        input(
            f'\nColoca aqui dados do cartão:\nAh, {name}, pode ficar relax que ninguém vai ter acesso a esses dados, tá?\n> ')
        bye(l, tot)

    elif s == 'cartão_de_débito' or s == 'CD':
        print(f'\nValor da compra: R$ {tot:.2f}')
        input(
            f'\nColoca aqui os dados do cartão:\nAh, {name}, pode ficar relax que ninguém vai ter acesso a esses dados, tá?\n> ')
        bye(l, tot)

    elif s == 'PIX' or s == 'pix':
        print(f'\nValor da compra: R$ {tot:.2f}\n')
        print('Pronto! Agora é fazer o PIX para o e-mail: professores.bcw4@soulcodeacademy.com')
        input('\nColoca aqui pra mim o comprovante da transferência:\n> ')
        bye(l, tot)


# ______________________________________________________________________________________________________________________________________________________________

# DECLARAÇÃO VARIÁVEIS:

list_adeq = [['Ração(R)', 'R'], ['Ração Premium(RP)', 'RP'], ['Brinquedo(BR)', 'BR'], ['Remédio(RM)', 'RM'],
             ['Tosa(T)', 'T'], ['Banho(B)', 'B'], ['Passeio(P)', 'P'], ['Hotel(H)', 'H']]
list_prod = [
    'Os produtos em estoque são:\n\n- Ração(R): R$ 199.90\n- Ração_Premium(RP): R$ 259.90\n- Brinquedo(BR): R$ 39.90\n- Remédio(RM): R$ 59.90']
list_serv = [
    'Os serviços disponíveis são:\n\n- Tosa(T): R$ 59.90\n- Banho(B): R$ 49.90\n- Passeio(P): R$ 39.90\n- Hotel(H): R$ 119.90']
list_main = []
carrinho = 0
y = 13457

# ______________________________________________________________________________________________________________________________________________________________

# INICIO CÓDIGO

name = input(f'Olá, cliente nº: {y}!\n\nPor favor, digite seu primeiro nome:\n> ')
y += 1
print(f'\nAgora sim, {name}!\nBem-vindo(a) a PetShopBoys: O parque de diversões dos "Pais de Pet"!')
while True:
    continuar = ' '  # input('\n\nEscolha Acessar(A) nosso menu ou Finalizar(F) o atendimento:\n> ').strip().upper()[0]

    # WHILE INPUT DIFERENTE DE F EXECUTAR O PROGRAMA

    while continuar not in 'AF':
        continuar = input('\n\nEscolha Acessar(A) nosso menu ou Finalizar(F) o atendimento:\n> ').strip().upper()[0]

        # IF INPUT SEJA A ABRIR MENU PARA O CLIENTE

        if continuar == 'A':
            call = input('\nPosso te ajudar com:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()
            while call not in 'P,SV,C,S':
                call = input(
                    '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()

            resp = ''

            while (resp != 'S'):

                # IF PARA CALLAR OS PRODUTOS

                if call == 'produtos' or call == 'PRODUTOS' or call == 'P':
                    print()
                    print(*list_prod, sep='')
                    prod = input('\nPõe aqui o código do produto que você escolheu: ').upper()
                    while prod not in 'R, RP, BR, RM':
                        prod = input('\nPõe aqui o código do produto que você escolheu: ').upper()
                    while True:
                        try:
                            qnt = int(input('Escolha a quantidade: '))
                            while qnt < 1:
                                qnt = int(input('Ops! Quantidade inválida, tente novamente: '))
                            break
                        except:
                            print('Número inválido')
                    val = val_prod(prod, qnt)
                    adequação = adeq(list_adeq, prod)
                    list_sub = [qnt, adequação, val]
                    list_main.append(list_sub)
                    carrinho += val
                    print(f'\n> Adicionei {qnt} unidades de {adequação} no seu carrinho.\n>> Total: R$ {val:.2f}')
                    call = input(
                        '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()
                    while call not in 'P,SV,C,S':
                        call = input(
                            '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()


                # ELIF PARA CALLAR OS SERVIÇOS

                elif (call == 'serviços' or call == 'SERVIÇOS' or call == 'SV'):
                    print()
                    print(*list_serv, sep='')
                    serv = input('\nPõe aqui o código do serviço desejado: ').upper()
                    while serv not in 'T, B, P, H':
                        serv = input('\nPõe aqui o código do serviço desejado: ').upper()
                    while True:
                        try:
                            qnt = int(input('Escolha a quantidade de vezes: '))
                            while qnt < 1:
                                qnt = int(input('Ops! Quantidade inválida, tente novamente: '))
                            break
                        except:
                            print('Número inválido')
                    val = val_serv(serv, qnt)
                    adequação = adeq(list_adeq, serv)
                    list_sub = [qnt, adequação, val]
                    list_main.append(list_sub)
                    carrinho += val
                    print(f'\n> Adicionei {qnt} vezes o serviço {adequação} no seu carrinho.\n>> Total: R$ {val:.2f}')
                    call = input(
                        '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()
                    while call not in 'P,SV,C,S':
                        call = input(
                            '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()

                # ELIF PARA CALLAR O CARRINHO

                elif (call == 'carrinho' or call == 'CARRINHO' or call == 'C'):

                    # IF PARA CARRINHO VAZIO

                    if carrinho == 0:
                        print('\nOps! Seu carrinho ainda está vazio! Vamos às compras!')
                        call = input(
                            '\nPosso te ajudar com:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()
                        while call not in 'P,SV,C,S':
                            call = input(
                                '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()


                    # ELSE EXIBIR LISTA MAIN = PRODUTOS NO CARRINHO

                    else:
                        print()
                        exibir_lista(list_main)
                        print('-' * 35)
                        print(f'Valor total: {carrinho:.2f}')

                        # INPUT/IF PARA REMOVER PRODUTOS DO CARRINHO

                        q = str(input(f'\n{name}, quer remover algum intruso dessa lista?\n(S/N): ')).strip().upper()[0]
                        while q not in 'SN':
                            q = \
                            str(input(f'\n{name}, quer remover algum intruso dessa lista?\n(S/N): ')).strip().upper()[0]
                        if q == 'S':
                            r = input('\nFala pra mim o código do item intruso:\n> ').upper()
                            while r not in 'R, RP, BR, RM, T, B, P, H':
                                r = input('\nFala pra mim o código do item intruso:\n> ').upper()
                            r = adeq(list_adeq, r)
                            i = identifica(list_main, r)
                            carrinho -= list_main[i][2]
                            list_main.pop(i)
                            print('\nProduto removido com sucesso!')

                        # IF PARA CALLAR CHECKOUT

                        checkout = input('\nTudo certo para finalizarmos a compra?\n(S/N): ').strip().upper()[0]
                        while checkout not in 'SN':
                            checkout = input('\nTudo certo para finalizarmos a compra?\n(S/N): ').strip().upper()[0]
                        if checkout == 'S':
                            metodo = input(
                                f'\n{name}, qual a forma de pagamento que você prefere?\n\nDinheiro(DR), PIX, Cartão de Crédito(CC), Cartão de Débito(CD) ou Desistir da Compra(D)?\n> ').upper()
                            resp = 'S'

                            # IF PARA DESISTÊNCIA DA COMPRA

                            if metodo == 'D' or metodo == 'DESISTIR':
                                print(
                                    f'\nCOMOASSIM, {name}?! Você realmente vai abandonar seu carrinho (e a mim também ;-;)?\n')
                                exibir_lista(list_main)
                                desist = input('(S/N): ').strip().upper()[0]
                                while desist not in "SN":
                                    desist = input('(S/N): ').strip().upper()[0]

                                # IF DESISTÊNCIA POSITIVA

                                if desist == 'S':
                                    print(f'\nUma pena você estar indo embora, {name}.')

                                # IF DESISTÊNCIA NEGATIVA

                                else:
                                    metodo = input(
                                        f'\nOba, você ficou! Qual forma de pagamento você prefere, {name}:\n\nDinheiro(DR), Cartão de Crédito(CC), Cartão de Débito(CD) ou PIX?\n> ').upper()
                                    pagamento(metodo, carrinho, list_main)

                            # ELSE O CLIENTE NÃO TENTE DESISTIR

                            else:
                                pagamento(metodo, carrinho, list_main)

                        # ELSE CASO O CLIENTE RESPONDA ALGO ERRADO NO MÉTODO DE PAGAMENTO

                        else:
                            call = input(
                                '\nCerto! Vamos para onde então:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()
                            while call not in 'P,SV,C,S':
                                call = input(
                                    '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()


                # ELIF CASO O CLIENTE DIGITE SAIR

                elif (call == 'sair' or call == 'SAIR' or call == 'S'):
                    resp = input(f'\nTem certeza que deseja sair, {name}? ;-;\n(S/N): ').strip().upper()[0]
                    while resp not in 'SN':
                        resp = input(f'\nTem certeza que deseja sair, {name}? ;-;\n(S/N): ').strip().upper()[0]

                    # IF CASO CLIENTE DESISTA DE SAIR

                    if resp != 'S':
                        call = input(
                            '\nOba, você ficou! Vamos para onde então:\n\nProdutos(P), Serviços(SV) ou Carrinho(C)?\n> ').upper()
                        while call not in 'P,SV,C,S':
                            call = input(
                                '\nVamos para onde agora:\n\nProdutos(P), Serviços(SV), Carrinho(C) ou Sair(S)?\n> ').upper()


                    # ELSE CASO CLIENTE PROSSIGA COM SAÍDA

                    else:
                        print(f'\nUma pena você estar indo embora, {name}. :(')

    # CONTINUAR PARA QUE AO FIM DO PROG RETORNE AO INÍCIO
    # IF CASO O CLIENTE DIGITE F TANTO NO INÍCIO QUANTO AO FIM

    if continuar == 'F':
        print(f'\n\nObrigado pela visita, {name}! \o/\nVolte sempre!')
        break
