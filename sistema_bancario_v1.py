menu = '''

[1] depositar 
[2] sacar
[3] extrato 
[4] sair  [ 
==>   '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':

        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n '

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == '2':
        valor = float(input('informe valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques= numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print('falha na operacao! voce nao tem o saldo nescessario')
            
        elif excedeu_saques:
            print('voce excedeu o limite de saques diarios')
        
        elif excedeu_limite:
            print('falha na operacao! voce excedeu limite na conta')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1


    elif opcao == '3':
         print('\n================ EXTRATO ================')
         print('Não foram realizadas movimentações.' if not extrato else extrato)
         print(f'\nnumero de saques disponiveis:{LIMITE_SAQUES - numero_saques} ')
         print(f'\nSaldo: R$ {saldo:.2f}')
         print('==========================================')
    elif opcao == '4':
         break

    else:
        print('operacao invalida, tente novamente')