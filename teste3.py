''' 3.1. Opcional: Fa¸ca um sistema banc´ario em que tenha uma classe geral
Conta. Devem haver outras duas classes, ContaCorrente e ContaPoupan¸ca,
que ir˜ao herdar da classe principal. As especifica¸c˜oes est˜ao abaixo:
• class Conta: * Vari´aveis globais/atributos: n´umero da conta, CPF do
cliente, agˆencia.
• class ContaCorrente: * Vari´aveis globais: n´umero da conta, CPF do
cliente, agˆencia. * M´etodos: saque(), dep´osito(), transferˆencia().
• class ContaPoupan¸ca: * Vari´aveis globais: n´umero da conta, CPF do
cliente, agˆencia. * M´etodos: rendimento().'''

class conta(num_conta, cpf, agencia):
    pass
    
    self.num_conta = num_conta
    self.cpf = cpf
    self.agencia = agencia 
    
    class conta_corrente(saque, deposito, transferecia):
        self.saque = saque
        self.deposito = deposito
        self.transferencia = trasnferencia
        
    class conta_poupanca(rendimento):
        self.rendimento


''' ---------------------------------------------------------------------------  entradas do programa'''
'''registro'''
nome = input("Insira o nome do usuario: ")
identidade =  input("Insira o numero de CPF cadastrado: ")
agencia =  input("Número da agência: ")
tipo_da_conta = input("Tipo da conta. corrente ou poupança: ")
valor_acumulado = input("Valor atual disponivel na conta: ")
operaçoes = input("Escolha o tipo de operação desejada (saque, depósito ou trasnferencia: ")
