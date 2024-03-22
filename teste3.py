''' 3.1. Opcional: Fa¸ca um sistema banc´ario em que tenha uma classe geral
Conta. Devem haver outras duas classes, ContaCorrente e ContaPoupan¸ca,
que ir˜ao herdar da classe principal. As especifica¸c˜oes est˜ao abaixo:
• class Conta: * Vari´aveis globais/atributos: n´umero da conta, CPF do
cliente, agˆencia.
• class ContaCorrente: * Vari´aveis globais: n´umero da conta, CPF do
cliente, agˆencia. * M´etodos: saque(), dep´osito(), transferˆencia().
• class ContaPoupan¸ca: * Vari´aveis globais: n´umero da conta, CPF do
cliente, agˆencia. * M´etodos: rendimento().'''

class Conta():
    def __init__(self, numero, cpf, agencia, saldo):
        self.numero = numero
        self.cpf = cpf
        self.agencia = agencia 
        self.saldo = saldo
        
    def info(self):
        print("=== Conta criada com sucesso!====")
        print("Número da Conta...:", self.numero)
        print("CPF do Titular....:", self.cpf)
        print("Agência...........:", self.agencia)
        print("Saldo.............:", self.saldo)
        print("----------------------------------")
        
class ContaCorrente(Conta):
    def __init__(self, numero, cpf, agencia, saldo):
        super().__init__(numero, cpf, agencia)
        self.saldo = saldo
        
    def saque(self, valor):
        self.saldo -= valor
        return print(f'Sucesso! Seu novo saldo é {self.saldo}')
        
    def deposito(self, valor):
        self.saldo += valor
        return print(f'Sucesso! Seu novo saldo é {self.saldo}')
    
    def transferencia(self, valor, conta_destino):  
        self.saldo -= valor
        conta_destino.saldo = self.conta_destino + valor
        return print(f'Sucesso! Seu novo saldo é {self.saldo} e o saldo do destino é {conta_destino.saldo}')
        
class ContaPoupanca(Conta):
    def __init__(self, numero, cpf, agencia, saldo):
        super().__init__(numero, cpf, agencia)
        self.saldo = saldo
        
    def rendimento(self, juros, meses):  
        self.saldo = self.saldo*(1 + juros)**meses
        return print(f'Seu montante atual é de {self.saldo} com tempo de {meses} meses')
        

print("Seja bem-vindo(a)! É um enorme prazer tê-lo no Ban[code], complete com suas informações para eu poder lhe ajudar :)") 
print()
name = input("Insira o nome completo do Titular: ").split()
account = "94837401841"
identity =  input("Insira o numero de CPF cadastrado: ")
agency =  input("Número da agência: ")

Titular1 = Conta(account, identity, agency, 0)
print()
print("Estamos preparando tudo para te receber...")
print()
print(f'Como é bom te ver de novo {name[0]}!')
print()
Titular1.info()
print()

print()

acc_type = 'X'
while acc_type != 'C' or acc_type != 'P':
    if acc_type != X:
        print("Ops! Tente novamente")
    acc_type = input("Qual o tipo da conta (C = corrente ou P = poupança)?")
if acc_type == 'C': # Conta Corrente
    print(f'Seu saldo atual da conta bancária é de R${Titular1.saldo},00')
    
    
    operation = input("Insira o valor da operação que deseja fazer (S = saque; D = depósito; T = transferencia):")
    
    if operation == 'S':
        valor_sacado = int(input("Insira o valor que deseja retirar: "))
        Titular1.saque(valor_sacado)
    elif operation == 'D':
        valor_depositado = int(input("Insira o valor que deseja depositar: "))
        Titular1.deposito(valor_depositado)
    elif operation == 'T':
        destino, valor_transferido = list(map, int(input("Insira a conta de destino e o valor que deseja transferir: ").split()))
        Titular1.transferencia(valor_transferido)
    else: 
        print("Ops! Essa não é uma operação válida")
else: # Conta Poupança
    print(f'Seu saldo atual da conta bancária é de R${saldo},00')


operation = input("Insira o valor da operação que deseja fazer (S = saque; D = depósito; T = transferencia):")
