from collections import deque  

def executar_lru(caminho_arquivo):
    capacidade_memoria = 8000  # Capacidade máxima da memória em quadros

    # Leitura e processamento da linha do arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        linha = "".join(arquivo.readlines()).replace("\n", "").strip()

    paginas_na_memoria = set()  # Conjunto para acesso rápido das páginas na memória
    ordem_acesso = []           # Lista para controlar a ordem de uso (LRU)
    cont = 0                    # Contador de page faults

    # Separa as referências por ';' e remove espaços
    lista_referencias = [ref.strip() for ref in linha.split(";")]

    # Encontra onde termina a sequência (marcador "0,0")
    indice_fim = lista_referencias.index("0,0") if "0,0" in lista_referencias else len(lista_referencias)

    # Processa cada referência de página até "0,0"
    for elemento in lista_referencias[:indice_fim]:
        if not elemento:
            continue  # Ignora entradas vazias

        processo_str, pagina_str = elemento.split(",")
        processo = int(processo_str)
        pagina = int(pagina_str)
        chave = (processo, pagina)

        if chave in paginas_na_memoria:
            # HIT: atualiza a ordem de acesso
            if chave in ordem_acesso:
                ordem_acesso.remove(chave)
            ordem_acesso.append(chave)
        else:
            # MISS: page fault
            cont = cont + 1
            if len(paginas_na_memoria) < capacidade_memoria:
                paginas_na_memoria.add(chave)
                ordem_acesso.append(chave)
            else:
                # Remove a menos recentemente usada
                chave_antiga = ordem_acesso.pop(0)
                paginas_na_memoria.remove(chave_antiga)
                paginas_na_memoria.add(chave)
                ordem_acesso.append(chave)

    # Exibe o total de page faults
    print("Page Faults:", cont)

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    executar_lru(nome_arquivo)
