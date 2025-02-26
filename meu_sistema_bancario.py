#deposito, saque e extrato
saldo = 0
limite_saque = 500
extrato = ""
num_saques = 0
QNTD_LIMITE_SAQUES = 3

menu = """
----------Menu----------

{d} - Depósito
{s} - Saque
{e} - Extrato
{x} - Sair

>>> Selecione: """

while True: 
    
    opcao = input(menu)

    if opcao == "d":

        print("\n------------------------- Depósito ----------------------------")

        valor = float(input("Digite a quantia desejada para fazer o depósito: "))

        if valor > 0:
            saldo += valor
            print("Valor depositado com sucesso!")
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Não será possível depositar uma quantia negativa de dinheiro em sua conta!")

    elif opcao == "s":

        print("\n------------------------- Saque ----------------------------")

        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:

            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite_saque:

            print("Operação falhou! O valor do saque excede o limite.")

        elif num_saques >= QNTD_LIMITE_SAQUES:

            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
    
        print("\n------------------------- Extrato ----------------------------")
        
        if extrato == "":
           
           print("\nNão foram feitas alterações nessa conta.")

        if extrato != "":
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "x":

        break

    else:
        print("Opção inválida, tente novamente.")
      




