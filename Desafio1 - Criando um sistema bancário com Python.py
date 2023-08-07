def depositar(saldo, extrato):
    valor_deposito = float(input("Informe o valor que deseja depositar: "))
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
        print(f"Depósito de {valor_deposito}, realizado com sucesso")
    else:
        print(f"Valor de {valor_deposito} inválido")
    return saldo, extrato

def sacar(saldo, extrato, numero_saque, limite_saque, limite_diario):
    valor_saque = float(input("Favor informe o valor que deseja sacar: "))

    if valor_saque >= saldo:
        print(f"Saldo insuficiente. Valor informado {valor_saque}, o saldo atual é de {saldo}")

    elif numero_saque >= limite_saque:
        print(f"Número de saques excedido. Limite de saque {limite_saque}, quantidade de saques já realizados {numero_saque}")

    elif valor_saque > limite_diario:
        print(f"Valor informado superior ao limite diário R$ {limite_diario}")

    elif valor_saque <= 0:
        print("Valor inválido")

    else:
        numero_saque += 1
        saldo -= valor_saque
        extrato += f"Saque de R$ {valor_saque:.2f}\n"
        print(f"Saque número {numero_saque}")
        print(f"Saque autorizado de R$ {valor_saque}, favor retirar as cédulas da máquina")
        print(f"Saldo restante: R$ {saldo:.2f}")

    return saldo, extrato, numero_saque

def exibir_extrato(saldo, extrato):
    print(f"\n===========Extrato===========")
    print("\n Não foram realizadas operações" if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("\n==============================")

def main():
    menu = """

    Escolha uma opção:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    => """

    saldo = 0
    limite_saque = 3
    extrato = ""
    numero_saque = 0
    limite_diario = 500

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == 2:
            saldo, extrato, numero_saque = sacar(saldo, extrato, numero_saque, limite_saque, limite_diario)

        elif opcao == 3:
            exibir_extrato(saldo, extrato)

        elif opcao == 0:
            print("Operação finalizada!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada!")

if __name__ == "__main__":
    main()
