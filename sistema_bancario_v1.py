saldo = 0
extrato = ''
saques = 0
LIMITES_SAQUES_DIARIOS = 3
LIMITES_SAQUES_VALOR = 500
menu = f'''
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
'''
print(f'''
{'=' * 40}
{'Sistema Bancário V1'.center(40)}
{'=' * 40}''')
while True:
    print(menu)
    opcao = input('Opção: ')
    print()

    if opcao == '1':
        valor = float(input('Informe o valor que deseja depositar: '))
        print()
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
            print(f'Deposito de R${valor:.2f} efetuado com sucesso.')
        else:
            print(f'Valor inválido para depósito.')
    
    elif opcao == '2':
      valor = float(input('Informe o valor deseja sacar: '))
      print()
      if saques >= LIMITES_SAQUES_DIARIOS:
          print('Você excedeu o número de saques diários.')
      elif valor >= LIMITES_SAQUES_VALOR:
          print('Você excedeu o limite de saque permitido pela conta.')
      elif valor > saldo:
          print('Você não tem saldo suficiente para realizar essa operação.')
      elif valor > 0:
          saques += 1
          extrato += f'Saque: R${valor:.2f}\n'
          saldo -= valor
          print(f'Saque de R${valor:.2f} realizado com sucesso.')
      else:
          print('O valor informado é inválido.')

    elif opcao == '3':
        print(f'Saldo disponível: R${saldo:.2f}')
        print()
        print(f'{extrato}' if extrato else 'Ainda não foram feitas transações nessa conta.')

    elif opcao == '4':
        print('Obrigado por usar nossos serviços. Até mais!')
    
    else:
        print('Opção inválida.')