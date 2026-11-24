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

    opção = input(menu)

    if opção == "d":
        valor = float(input("Quanto deseja depositar?"))
        if valor >0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"Depósito de R${valor} efetuado com sucesso.")
        else:
            print("Erro no depósito, depositar uma quantia maior que R$0.00.")    

    elif opção == "s":
        saque = float(input("Quanto você deseja sacar?"))
        if saldo >0:
            if saque <= saldo:
                if saque > limite:
                   print(f"O valor do saque ultrapassou o limite de R${limite}")
                   continue
                
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque de R${saque:.2f}\n"
                print(f"Saque de R${saque} efetuado com sucesso.")
                
        else:
            print("Saldo Insuficiente.")       

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diários atingido!.")          
            continue


    elif opção == "e":
        print(extrato)

    elif opção == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")