Menu = """
---------------------------------------------
            Bem-vindo ao Dubank

[1] Depósitar
[2] Sacar
[3] Ver extrato
[4] Sair

Oque você deseja fazer?: \n"""

saldo = 0
deposito = 0
saques_feitos = 0
saques_diarios = 3
extrato = ""
limite_de_saque_por_vez = 500

while True:
    
    opcao = input(Menu)

    if opcao == "1":

        d = int(input("Quanto deseja depósitar?: "))
        print(d)

        if d == float:
            print("Operação falhou, não se pode fazer depositos com números quebrados, coloque um número inteiro.")

        elif d <= 0:
            print("Operação falhou, não se pode depósitar números negativos ou 0 na sua conta.)")

        else:
            saldo += d
            deposito += 1 

            extrato += f"Deposito: R${d: .2f} \n"
            print (saldo)
        
    elif opcao == "2":
        s = int(input("Quanto deseja sacar?: "))
        print(s)

        if saldo <= 0:
            print("Operação falhou, você não tem saldo.")

        elif s > saldo:
            print(f"Operação falhou, o valor de saque é maior do que o seu saldo \nesse é o seu saldo: {saldo}")

        elif s > limite_de_saque_por_vez:
            print("Operação falhou, o seu saque é maior do que o limite permitido. (limite: R$ 500,00)")

        elif saques_feitos == saques_diarios:
            print("Operação falhou, você atingiu o seu limite de saques diarios, volte amanhã.")
        
        elif s <= 0:
            print("Operação falhou, não se pode sacar números negativos ou 0 da conta.") 

        elif s < saldo:
            saldo -= s
            saques_feitos += 1

            extrato += f"Saque: R${s:.2f} \n"

            print(f"Saque feito com sucesso!")

    elif opcao == "3":
       print("================== Extrato ====================")
       print("Não foram realizadas movimentações" if not extrato else extrato) # Aqui será exibido a mensagem se a variavel extrato estiver vazia, mas se não ele irá mostrar oque tem dentro da variavel
       print("")
       print(f"Saldo: R${saldo:.2f}")
       print("")
       print("===============================================")


        

    elif opcao == "4":
        print("Obrigado por utilizar o serviço do Dubank, tenha uma ótima semana! ")
        break
    else:
        print("Operação falhou, a opção escolhida não é existente no sistema, escolha alguma em exibição \npor favor!") 