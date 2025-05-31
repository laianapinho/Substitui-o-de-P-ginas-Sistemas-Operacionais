from fifo import executar_fifo  
from segundachance import executar_segundachance
from lru import executar_lru


def algoritmo_1():
    print("Algoritmo 1: Fifo")
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    executar_fifo(nome_arquivo)          

def algoritmo_2():
    print("Algoritmo 2: LRU")
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    executar_lru(nome_arquivo)    

def algoritmo_3():
    print("Algoritmo 3: Segunda Chance")
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    executar_segundachance(nome_arquivo)    

def algoritmo_4():
    print("Executa todos")
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    executar_fifo(nome_arquivo)
    executar_lru(nome_arquivo)   
    executar_segundachance(nome_arquivo)        

def algoritmo_padrao():
    print("Número inválido. Escolha entre 1, 2, 3 ou 4.")

# Mapeamento dos algoritmos
algoritmos = {
    1: algoritmo_1,
    2: algoritmo_2,
    3: algoritmo_3,
    4: algoritmo_4
}

# Programa principal
print("Escolha um algoritmo para executar:")
print("1 - Algoritmo FIFO")
print("2 - Algoritmo LRU")
print("3 - Algoritmo Segunda Chance")
print("4 - Todos")

opcao = int(input("Digite o número do algoritmo (1-4): "))

# Executa o algoritmo escolhido ou o padrão
algoritmos.get(opcao, algoritmo_padrao)()