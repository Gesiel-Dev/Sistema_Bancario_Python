import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            data_hora_saque = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            extrato += f"Saque: R$ {valor:.2f} - Data e Hora: {data_hora_saque}\n"
            numero_saques += 1
            saques_restantes = LIMITE_SAQUES - numero_saques
            print(f"Saque realizado com sucesso! Você ainda pode realizar {saques_restantes} saques hoje.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "q":
        print("Obrigado por Utilizar nosso Sistema!")
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")