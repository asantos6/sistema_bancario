menu = """

Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUE = 3


while True:

    opcao = int(input(menu))
    
    if opcao == 1:
        valor_deposito = float(input("Informe o valor que deseja depositar "))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato += f"Depósito de R$ {valor_deposito: .2f}\n"
            print(f"Deposito de {valor_deposito}, realizado com sucesso")

        else:
            print(f"Valor de {valor_deposito} inválido")

    elif opcao == 2:

        valor_saque = float(input("Favor informe o valor que deseja sacar: "))

        if valor_saque >= saldo:
            print(f"Saldo insuficiente.Valor informado {valor_saque}, o saldo atual é de {saldo}")

        elif numero_saque >= LIMITE_SAQUE:
            print(f"Numero de saque excedido. Limite de saque {LIMITE_SAQUE}, quantidade de saque já realizado {numero_saque}")
    
        
        elif valor_saque > limite:
            print(f"Valor informado superior ao limite diário R$ {limite}")
        
        elif valor_saque <= 0:
            print("Valor inválido")

        
        else:
            numero_saque = numero_saque+1
            saldo=saldo-valor_saque
            extrato += f"Saque de R$ {valor_saque: .2f}\n"
            print(f"saque numero {numero_saque}")
            print(f"Saque autorizado de R$ {valor_saque} , favor retire as cedulas da maquina")
            print(saldo)

    elif opcao == 3:

        print(f"\n===========Extrato===========")
        print("\n Não foram realizadas operações" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n==============================")

    elif opcao == 0:
        print("Operação finalizada!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")          


    