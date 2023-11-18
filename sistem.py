import os
import time
import sys


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def loading_animation(self):
        bar_width = 20
        sys.stdout.write("[%s]" % (" " * bar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (bar_width + 1))

        for i in range(bar_width):
            time.sleep(0.1)  # Simulando alguma tarefa
            sys.stdout.write("-")
            sys.stdout.flush()

        sys.stdout.write("]\n")
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Saque não permitido. Saldo insuficiente.')

    def verificar_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')



os.system("cls")
nome_usuario = input("Digite seu nome: ")
conta_usuario = ContaBancaria(nome_usuario)

while True:
    print("\nOpções:")
    print("1. Verificar Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == "1":
        conta_usuario.loading_animation()
        os.system("cls")
        conta_usuario.verificar_saldo()
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        conta_usuario.loading_animation()
        os.system("cls")
        conta_usuario.depositar(valor_deposito)
    elif opcao == "3":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        conta_usuario.loading_animation()
        os.system("cls")
        conta_usuario.sacar(valor_saque)
    elif opcao == "4":
        conta_usuario.loading_animation()
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")