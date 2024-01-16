from datetime import datetime

saldo = 0
extrato = []
num_saque = 0



# --------- menu ---------- #

menu = """
------ M E N U ------ 

    [S] = SAQUE
    [D] = DEPOSITO
    [E] = EXTRATO
    [Q] = SAIR

------ BANCO GT ------

=>

"""


#Deposito - Não deixar depositar valores negativos - Constar todos os depositos em extrato

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
              

#saque - só pode no maximo 3 por dia - limite de 500 por saque - usuario com saldo negativo deve ser informado - todos os saques deve ser exibidos em extrato

def saque(valor):
    global num_saque,saldo,extrato

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
        num_saque=+ 1
        extrato.append(f"Saque realizado no valor de R$ {valor:.2f}. {periodo()} ")
        return print(f"Saque efetuado no valor de R$ {valor:.2f}. Seu saldo é: R$ {saldo:.2f}")


#Extrato - listar todos os depositos e saques da conta - exibir no final o saldo da conta - valores deve ser exibido no seguinte formato(R$ 1.500,00)
    
def funcao_extrato():
    global extrato,saldo

    for extr in extrato:
        print(f"{extr}") 
    print(f"Saldo em conta: {saldo:.2f}")



#Função para marcar a hora do deposito
    
def periodo():
    hora_atual = datetime.now()
    data_atual = datetime.now().date()
    return f"Data: {data_atual.day:02d}/{data_atual.month:02d}/{data_atual.year} Horario: {hora_atual.hour:02d}:{hora_atual.minute:02d}."



#loop Menu

while True:
    
    escolha = input(menu)

    try:
        if escolha.upper() == "S" :

            while True:
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
                        saque(valor)
                        break
                    except ValueError:
                        vl_saque = input("Por favor, insira um valor numérico válido ou [S] para sair.")          
                        if vl_saque.upper() == "S":
                            print("Volte sempre!")
                            break
                break               

        elif escolha.upper() == "D" :
            
            vl_deposito = input("Digite a quantia que deseja depositar.): ")
            deposito(vl_deposito)    
     
        elif escolha.upper() == "E" :
            funcao_extrato()
            break
        
        elif escolha.upper() == "Q" :
            break
    except ValueError:
        vl_saque = input("Por favor, insira um parâmetro válido ou [Q] para sair.")          
        if vl_saque.upper() == "Q":
            break      






     