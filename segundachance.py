def executar_segundachance(caminho_arquivo):
    capacidade_memoria = 8000  # Define a capacidade máxima da memória em quadros (páginas armazenáveis)

    # Leitura e processamento da linha do arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        linha = "".join(arquivo.readlines()).replace("\n", "").strip()
        # Lê todas as linhas do arquivo, remove quebras de linha e espaços extras, formando uma string única

    # Separa as referências por ';' e remove espaços
    lista_referencias = [ref.strip() for ref in linha.split(";")]
    # Divide a string por ';' para obter cada referência de página, e remove espaços em branco

    # Encontra onde termina a sequência (marcador "0,0")
    indice_fim = lista_referencias.index("0,0") if "0,0" in lista_referencias else len(lista_referencias)
    # Localiza o índice onde está o marcador "0,0", que indica o fim da sequência; se não houver, considera toda a lista

    fila_circular = []  # Lista que armazena as páginas na memória (funciona como fila circular)
    mapa_bits = {}      # Dicionário que armazena o bit de referência de cada página (0 ou 1)
    ponteiro = 0        # Índice atual da fila circular, simulando o ponteiro do "relógio"
    cont = 0            # Contador de page faults

    # Itera sobre cada referência até o marcador "0,0"
    for elemento in lista_referencias[:indice_fim]:
        processo_str, pagina_str = elemento.split(",")     # Separa a referência em processo e página
        processo = int(processo_str)                        # Converte o número do processo para inteiro
        pagina = int(pagina_str)                            # Converte o número da página para inteiro
        chave = (processo, pagina)                          # Cria uma tupla para representar a página referenciada

        if chave in fila_circular:
            mapa_bits[chave] = 1  # A página está na memória, então marca como recentemente usada (bit = 1)
        else:
            cont = cont + 1       # Page fault: a página não estava na memória

            if len(fila_circular) < capacidade_memoria:
                # Ainda há espaço na memória, apenas adiciona a página
                fila_circular.append(chave)
                mapa_bits[chave] = 1 
            else:
                # Memória cheia — aplica o algoritmo de Segunda Chance (relógio)
                while True:
                    pagina_atual = fila_circular[ponteiro]  # Página apontada atualmente pelo "relógio"

                    if mapa_bits[pagina_atual] == 0:
                        # Página não foi usada recentemente — substitui por nova página
                        mapa_bits.pop(pagina_atual)        # Remove do dicionário de bits
                        fila_circular[ponteiro] = chave     # Substitui a página antiga pela nova na mesma posição
                        mapa_bits[chave] = 1                # Marca a nova página como recentemente usada
                        ponteiro = (ponteiro + 1) % len(fila_circular)  # Avança o ponteiro circularmente
                        break  # Página substituída — sai do loop
                    else:
                        # Página foi usada recentemente — zera o bit e dá segunda chance
                        mapa_bits[pagina_atual] = 0
                        ponteiro = (ponteiro + 1) % len(fila_circular)  # Avança o ponteiro circularmente

    # Exibe o total de page faults ocorridos
    print("Page Faults:", cont)
