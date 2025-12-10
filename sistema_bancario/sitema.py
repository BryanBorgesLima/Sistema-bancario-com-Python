menu = """
 [D]Deposito
 [S]Saque
 [E]Extrato
 [SR]Sair
 """
total_deposito = 0
total_saque = 0
limite = 500
saldo = 0
saque = 0
saques_realizados = 0
QUANTIDADE_SAQUE = 3

while True:
    opcao = (input(menu))

    if opcao == 'd':
        deposito = int(input('Quanto dejesa depositar: '))
        print(f'Você depositou R${deposito}')
        saldo += deposito
        total_deposito += deposito
       
    elif opcao == 's':

        if QUANTIDADE_SAQUE <= saques_realizados:
            print('Você não pode sacar mais')
            print(f'Você realizou: {saques_realizados} saques')
            continue
            

        saque = int(input('O quanto você deseja sacar: '))

        if saque >= 500:
            print('Você não pode sacar mais de R$500')
            continue
        if saque < saldo: 
         saldo -= saque
         print(f'Você sacou: R${saque}')
         saques_realizados += 1
         total_saque += saque
        else:
            print('Você nâo possui esse dinheiro')
            print(f'Você tem: R${saldo}')

    elif opcao == 'e':
        print(f"Você tem: R${saldo}")
        print(f'Você sacou o total de: R${total_saque}')
        print(f'Você depositou o total de: R${total_deposito}')
    
    elif opcao == 'sr':
        print("Obrigado por usar o programa!!")
        break    