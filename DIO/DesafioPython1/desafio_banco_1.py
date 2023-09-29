menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
extrator = []
extrato_depositos = []
extrato_saques = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": ##DEPOSITOS
        deposito = int(input("Quanto deseja depositar? "))
        saldo = saldo + deposito
        print(f"Depósito realizado com sucesso. Saldo: R$ {saldo}.")
        extrato_depositos.append(deposito)
        extrator.append(f"Deposito - R${deposito}")

    elif opcao == "s": ##SAQUES
        saque = int(input("Quanto deseja sacar? "))
        if numero_saques < 3:
            if saque <= saldo and saque <= limite:
                saldo = saldo - saque
                print(f"Saque realizado com sucesso, seu novo saldo é: R$ {saldo}.")
                extrato_saques.append(saque)
                extrator.append(f"Saque - R${saque}")
                numero_saques = numero_saques + 1
            
            elif saque > limite:
                print("O valor do saque excede o limite de saque.")

            elif saque > saldo:
                print("Saldo insuficiente.")
        else:
            print("Numero de saques diários excedidos.")

    elif opcao == "e": ##EXTRATO
        print("##EXTRATO##\n")
        
        if len(extrato_depositos) == 0 and len(extrato_saques) == 0:
            print("Não foram realizadas movimentações.")

        else:
            for i in extrator:
                print(i)
            # for operacoes in extrato_depositos:
            #     print(f"Deposito - R$ {operacoes}")
            # for operacoes in extrato_saques:
            #     print(f"Saque - R$ {operacoes}")
            # print(f"Seu saldo é de: R$ {saldo}.")
    
    elif opcao == "q": ##SAIR
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
