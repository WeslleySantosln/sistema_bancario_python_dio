# Banco GT - Simulação de Sistema Bancário em Python

Este repositório contém um projeto em Python que simula um sistema bancário básico com funcionalidades de saque, depósito e extrato. O objetivo é fornecer uma experiência simples de interação bancária.

## Funcionalidades

1. **Saque:** Realize saques com um limite máximo de R$ 500,00 por operação. Cada usuário pode realizar até 3 saques por dia.

2. **Depósito:** Faça depósitos, sendo importante notar que valores negativos não são permitidos. Todos os depósitos são registrados no extrato.

3. **Extrato:** Visualize o extrato da conta, que lista todas as operações de depósito e saque, incluindo a data e horário de cada transação. O saldo atual da conta também é exibido.

4. **Encerrar:** Saia do sistema a qualquer momento.

## Como Usar

Execute o script `banco_gt.py` para iniciar o sistema. Siga as instruções apresentadas no menu para interagir com as funcionalidades do banco.

## Exemplos de Uso

```python
# Exemplo de depósito
vl_deposito = input("Digite a quantia que deseja depositar: ")
deposito(vl_deposito)

# Exemplo de saque
vl_saque = input("Digite um valor para saque: ")
saque(valor)

# Exemplo de visualização de extrato
funcao_extrato()
