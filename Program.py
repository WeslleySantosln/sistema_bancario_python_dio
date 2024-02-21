from datetime import datetime

num_saque = 0
agencia = "AG: 0001"
saldo = 100
extrato = []
num_conta = []
usuarios = []
contas_corrente = []


menu = """
------ M E N U ------ 

    [S] = SAQUE
    [D] = DEPOSITO
    [E] = EXTRATO
    [T] = CRIAR CONTA CORRENTE
    [Q] = SAIR
    [C] = CADASTRAR USUARIOS
    [L] = LISTAR CONTAS

------ BANCO GT ------

=>

"""


#Deposito
#Não deixar depositar valores negativos
#Constar todos os depositos em extrato
#Deve receber os argumentos por posição 

def deposito(valor):
    global saldo,extrato
   
    try:
        valor = float(valor)
        if valor < 0:
            print("Valor negativo não permitido. Refaça a operação!")
            valor = input("Por favor, insira um valor numérico válido ou [S] para sair.")
            if valor.upper() == "S":
                print("Volte sempre!")
                           
            else:
                deposito(valor) 
                
        else:
            saldo += valor
            extrato.append(f"Deposito realizado no valor de R$ {valor:.2f}. {periodo()} ")  
            print(f"Deposito efetuado com sucesso. Seu saldo: R$ {saldo:.2f}")  
              
    except ValueError:
        valor = input("Por favor, insira um valor numérico válido ou [S] para sair.")          
        if valor.upper() == "S":
            print("Volte sempre!")
                        
        else:
            deposito(valor)
              

#saque
#só pode no maximo 3 por dia - limite de 500 por saque - usuario com saldo negativo deve ser informado - todos os saques deve ser exibidos em extrato
#Receber argumentos POR NOME
def saque(valor="none",extrato="none"):
    global saldo, num_saque

    if num_saque == 3:
        return print("Numero de saque excedido")
    elif valor > 500 :
        return print(f"Limite maximo para saque: R$ 500,00. Valor inserido: R$ {valor:.2f}")
    elif valor > saldo :
        return print(f"Valor para saque maior que o saldo da conta. Saldo da conta: R$ {saldo:.2f}, Valor de saque: R$ {valor:.2f}.")
    elif valor < 0 :
        return print("Porfavor coloque um numero posito!")
    else:
        saldo -= valor
        num_saque += 1
        extrato.append(f"Saque realizado no valor de R$ {valor:.2f}. {periodo()} ")
        return print(f"Saque efetuado no valor de R$ {valor:.2f}. Seu saldo é: R$ {saldo:.2f}")


#Extrato - listar todos os depositos e saques da conta - exibir no final o saldo da conta - valores deve ser exibido no seguinte formato(R$ 1.500,00)
#Deve receber os argumentos por posição e por nome, Posicional: saldo - Nomeados: extrato    
def funcao_extrato(extrato,/,saldo):
    
    for extr in extrato:
        print(f"{extr}") 
    print(f"Saldo em conta: {saldo:.2f}")



#Função para marcar a hora do deposito    
def periodo():
    hora_atual = datetime.now()
    data_atual = datetime.now().date()
    return f"Data: {data_atual.day:02d}/{data_atual.month:02d}/{data_atual.year} Horario: {hora_atual.hour:02d}:{hora_atual.minute:02d}."




#Criar função: Criar usuario

# O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço.
# O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF.
# Não podemos cadastrar 2 usuários com o mesmo CPF.

def cadastrar_usuario(nome,data_nascimento, cpf, endereco,agencia):
    global usuarios

    x = f"CPF: {cpf}"
    check_cpf = list(filter(lambda sublista: x in sublista, usuarios))


    if check_cpf:
        print("Usuario já cadastrado")
    else:
        user  = [f"CPF: {cpf}", f"Nome: {nome}", f"Data Nascimento:{data_nascimento}", f"Endereço:{endereco}",agencia]
        usuarios.append(user)         
        print(f"Usuario: {user} Cadastrado com sucesso. ")
        criar_corrente(cpf,agencia)






# uma conta é composta por: agência, número da conta e usuário.
# O número da conta é sequencial, iniciando em 1. 
# O número da agência é fixo: 0001.
# O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
# Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

def criar_corrente(cpf,agencia):
    global contas_corrente, num_conta
    
    i = f"CPF: {cpf}"
    check_usuario  = list(filter(lambda sublista: i in sublista, usuarios))
    check_conta_corrente  = list(filter(lambda sublista: i in sublista, contas_corrente))

    
    if check_conta_corrente:
        print("Usuario já possui uma conta")
        x = input("Deseja cadastar outra conta? [S/N] " )
        if x.upper() == "S":
            num_conta += 1
            contas_corrente.append([agencia,f"Numero da conta: {num_conta}",f"CPF: {cpf}"])  
    elif check_usuario:
        num_conta += 1
        contas_corrente.append([agencia,f"Numero da conta: {num_conta}",f"CPF: {cpf}"])
    else:
        print("CPF Não cadastrado como usuario, por favor, primeiro cadastre como usuario!")


#Listar contas
def listar_contas(cpf):

    x = False  
    for contas in contas_corrente:
        if contas[2] == f"CPF: {cpf}":
            print(contas)
            x = True

    if x == False:
        print("CPF não cadastrado!")    
    
        


#loop Menu
def main():

    while True:
        
        escolha = input(menu)

        try:

            #Sacar
            if escolha.upper() == "S" :
         
                vl_saque = input("Digite um valor para saque (Obs: O valor para saque é no maximo R$ 500,00.): ")
                while True:
                    try:
                        valor = float(vl_saque)
                        if valor < 0:
                            vl_saque = input("Por favor, insira um valor numérico válido ou [S] para sair.")          
                            if vl_saque.upper() == "S":
                                print("Volte sempre!")
                                break
                            continue
                        saque(valor=valor,extrato=extrato)
                        break
                    except ValueError:
                        vl_saque = input("Por favor, insira um valor numérico válido ou [S] para sair.")          
                        if vl_saque.upper() == "S":
                            print("Volte sempre!")
                            break
                                  
            #Depostiar                    
            elif escolha.upper() == "D" :
                
                vl_deposito = input("Digite a quantia que deseja depositar.): ")
                deposito(vl_deposito)    
            #Função extrato
            elif escolha.upper() == "E" :
                funcao_extrato(extrato, saldo=saldo)
                break

            #CADASTAR USUÁRIO   
            elif escolha.upper() == "C" :
                print("Digite os dados do usuario: (nome,data_nascimento, cpf, endereco,user)")
                nome = input("Nome: ")
                data_nascimento = input("data_nascimento: ")
                cpf = input("cpf: ")
                endereco = input("endereco: ")
                cadastrar_usuario(nome,data_nascimento, cpf,endereco,agencia)
           
            #Criar conta corrente
            elif escolha.upper() == "T" :
                print("Digite os dados do usuario que deseja criar a C/C: (CPF)")
                cpf = input("CPF: ")
                criar_corrente(cpf,agencia)
            #Listar contas
            elif escolha.upper() == "L" :
                print("Digite o CPF que deseja listar as contas)")
                cpf = input("CPF: ")
                listar_contas(cpf)

            #Sair
            elif escolha.upper() == "Q" :
                break
        except ValueError:
            vl_saque = input("Por favor, insira um parâmetro válido ou [Q] para sair.")          
            if vl_saque.upper() == "Q":
                break      
               



main()



     