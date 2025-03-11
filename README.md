Sistema_Bancario_com_Python

Este é um simples sistema bancário desenvolvido em Python para realizar operações bancárias básicas. As funcionalidades incluem depósito, saque, e exibição de extrato. O sistema utiliza um menu interativo para permitir que o usuário selecione a operação desejada.

Funcionalidades Depósito: Permite que o usuário deposite um valor positivo na conta. O saldo é atualizado e o valor do depósito é registrado no extrato.

Saque: Permite que o usuário saque um valor, desde que:

O valor do saque não exceda o saldo disponível.

O valor do saque não exceda o limite de saque diário de R$500.

O número de saques não exceda o limite de 3 saques diários.

O valor do saque é subtraído do saldo e registrado no extrato junto com a data e hora do saque.

Extrato: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual da conta.

Sair: Encerra o sistema bancário.
