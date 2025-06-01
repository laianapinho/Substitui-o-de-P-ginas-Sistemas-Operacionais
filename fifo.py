from collections import deque  

def executar_fifo(caminho_arquivo):
    capacidade_memoria = 8000  # Define a capacidade da memória (8.000 quadros de página)

    # Abre o arquivo de entrada no modo leitura
    with open(caminho_arquivo, 'r', encoding='utf-8-sig') as arquivo:
        # Lê todas as linhas, junta em uma única string, remove quebras de linha e espaços nas extremidades
        linha = "".join(arquivo.readlines()).replace("\n", "").strip()  

    fila_fifo = deque()  # Cria uma fila FIFO vazia para controlar a ordem de chegada das páginas
    paginasnamemoria = set()  # Cria um conjunto para armazenar as páginas que estão na memória (para acesso rápido)
    cont = 0  # Inicializa o contador de page faults

    # Divide a linha em uma lista de referências usando ";" como separador
    lista_referencias = [ref.strip() for ref in linha.split(";")]

    # Encontra o índice onde está o marcador "0,0" que indica o fim da sequência
    indice_fim = lista_referencias.index("0,0")  

    # Percorre a lista de referências até o índice do "0,0"
    for elemento in lista_referencias[:indice_fim]:
        
        # Separa cada referência no formato processo,pagina
        processo_str, pagina_str = elemento.split(",")
        processo = int(processo_str)  # Converte o processo para inteiro
        pagina = int(pagina_str)      # Converte a página para inteiro

        chave = (processo, pagina)  # Cria uma tupla (processo, pagina) que representa a página requisitada

        # Verifica se a página já está na memória (HIT)
        if chave in paginasnamemoria:
            continue  # Se sim, não gera page fault, segue para a próxima referência

        else:
            cont = cont + 1  # Se não, gera um page fault (FALHA DE PÁGINA)

            # Se ainda há espaço na memória
            if len(paginasnamemoria) < capacidade_memoria:
                fila_fifo.append(chave)       # Adiciona a página no final da fila (ordem de chegada)
                paginasnamemoria.add(chave)   # Adiciona no conjunto de páginas na memória

            else:
                # Memória cheia: remove a página mais antiga (FIFO)
                removido = fila_fifo.popleft()   # Remove da fila a página que entrou primeiro
                paginasnamemoria.remove(removido)  # Remove do conjunto de páginas na memória

                # Adiciona a nova página requisitada
                fila_fifo.append(chave)       
                paginasnamemoria.add(chave)   

    # Imprime o total de page faults encontrados
    print("Page Faults:", cont)


