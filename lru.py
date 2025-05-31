from collections import deque  
# Importa deque da biblioteca collections (não utilizado neste código, pode ser removido)

def executar_lru(caminho_arquivo):
    capacidade_memoria = 8000  # Capacidade máxima de páginas que cabem na memória

    # Leitura e processamento da linha do arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        linha = "".join(arquivo.readlines()).replace("\n", "").strip()
        # Lê todo o conteúdo do arquivo, remove quebras de linha e espaços extras

    paginas_na_memoria = set()  # Conjunto que mantém as páginas atualmente na memória (para acesso rápido)
    ordem_acesso = []           # Lista que mantém a ordem em que as páginas foram acessadas (para aplicar LRU)
    cont = 0                    # Contador de page faults (faltas de página)

    # Separa as referências por ';' e remove espaços em branco
    lista_referencias = [ref.strip() for ref in linha.split(";")]

    # Encontra o índice onde está o marcador de fim ("0,0")
    indice_fim = lista_referencias.index("0,0") if "0,0" in lista_referencias else len(lista_referencias)

    # Itera sobre as referências de página até "0,0"
    for elemento in lista_referencias[:indice_fim]:
        if not elemento:
            continue  # Ignora entradas vazias

        processo_str, pagina_str = elemento.split(",")  # Separa processo e página
        processo = int(processo_str)                    # Converte processo para inteiro
        pagina = int(pagina_str)                        # Converte página para inteiro
        chave = (processo, pagina)                      # Cria uma tupla (processo, página) para representar a referência

        if chave in paginas_na_memoria:
            # HIT: a página já está na memória, só precisa atualizar a ordem de uso
            if chave in ordem_acesso:
                ordem_acesso.remove(chave)              # Remove a chave da posição antiga na ordem
            ordem_acesso.append(chave)                  # Adiciona a chave ao final (mais recentemente usada)
        else:
            # MISS: a página não está na memória (page fault)
            cont = cont + 1

            if len(paginas_na_memoria) < capacidade_memoria:
                # Ainda há espaço na memória: apenas adiciona a nova página
                paginas_na_memoria.add(chave)
                ordem_acesso.append(chave)
            else:
                # Memória cheia: remove a menos recentemente usada (primeiro da lista)
                chave_antiga = ordem_acesso.pop(0)      # Remove a página mais antiga (LRU)
                paginas_na_memoria.remove(chave_antiga) # Remove do conjunto de páginas na memória
                paginas_na_memoria.add(chave)           # Adiciona a nova página
                ordem_acesso.append(chave)              # Marca como a mais recentemente usada

    # Exibe o total de page faults ao final
    print("Page Faults:", cont)
