def deposit(balance, account_statement):
    value = 0

    value = float(input('Informe o valor que deseja depositar: '))
    
    if (value > 0):
        balance += value        
        account_statement += f"Depósito: R$ {value:.2f}\n"
    
    else:
        print('Operação falhou! O valor informado é inválido.')
    
    return balance, account_statement
    
def withdrawal(balance, withdrawals, MAX_WITHDRAWAL, WITHDRAWALS_LIMIT, account_statement):
    value = float(input('Informe o valor que deseja sacar: '))

    balance_exceded = value > balance
    withdrawals_exceded = withdrawals >= WITHDRAWALS_LIMIT
    max_withdrawal_exceded = value > MAX_WITHDRAWAL
    
    if (balance_exceded):
        print('Não há saldo suficiente para realizar a operação.')
    elif (withdrawals_exceded):
        print('Limite diário de saques atingido.')
    elif (max_withdrawal_exceded):
        print('Valor é maior que o limite máximo de saque.')
    elif (value > 0):   
        balance -= value
        account_statement += f"Saque: R$ {value:.2f}\n"
        withdrawals += 1
    
    else:
        print('Operação falhou! O valor informado é inválido.')
    
    return balance, account_statement, withdrawals

def main():  
    balance = 0
    MAX_WITHDRAWAL = 500
    account_statement = ""
    withdrawals = 0
    WITHDRAWALS_LIMIT = 3
    
    menu = """

    Selecione uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
      
      opcao = input(menu)
      
      if opcao == "d":
        print('Deposito: ', end="\n\n")
        balance, account_statement = deposit(balance, account_statement)

      elif opcao == "s":
        print('Saque: ', end="\n\n")
        balance, account_statement, withdrawals = withdrawal(balance, withdrawals, MAX_WITHDRAWAL, WITHDRAWALS_LIMIT, account_statement)

      elif opcao == "e":
        print(' Extrato '.center(60, '#'))
        print('Sem movimentações.' if not account_statement else account_statement, end='')
        print(f"\nSaldo: R$ {balance:.2f}:")
        print(''.center(60, '#'))
      
      elif opcao == "q":
        break
      
      else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
if __name__ == '__main__':
    main()