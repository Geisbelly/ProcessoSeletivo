from funcs import *

print("Questão 1 - Usando a Estrutura de uma Lista")
n = int(input("Digite um número desejado: "))
print("\n"+fib(n))

#mania adivinda de orientação à objeto e estrutura de dados
print("\nQuestão 1 - Usando a Estrutura de uma Pilha")
n = int(input("Digite um número desejado: "))
pilha = fibonate()
print("\n"+pilha.fibo(n))

print("\nQuestão 2 - Simples")
string = input("Digite uma palavra ou texto: ")
print(verificarStringA("\n"+string))

#mania adivinda de orientação à objeto
print("\nQuestão 2 - Em Classe")
string = input("Digite uma palavra ou texto: ")
letra = input('Qual letra você deseja verificar? ')
estrutura = verificarString(letra)
estrutura.string(string)
print(estrutura.getDados())
