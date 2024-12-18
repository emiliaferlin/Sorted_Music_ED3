import time

def buscaTabelaHash(lista, valor):
    tabela_hash = {}
    # faz a enumeração da tabela
    for i, item in enumerate(lista):
        prefix = item[:len(valor)] # Extrai o prefixo do mesmo tamanho que o valor buscado
        if prefix not in tabela_hash:
            tabela_hash[prefix] = [] # Se não existir um prefixo
        tabela_hash[prefix].append(i) # Adiciona o índice do item na lista - pelo prefixo
    return tabela_hash.get(valor, [])

def main():
    #%%MIDI program teste
    valorBusca = input("Digite a nota que deseja encontrar: ").strip()
    if not valorBusca:
        print("Erro: Nenhum valor foi inserido. Por favor, tente novamente.")
        exit()

    # Processa o arquivo e realiza a busca por linha
    with open('52.txt', 'r') as file:
        linhas = file.readlines()  # Lê cada linha do arquivo como um item de lista

    inicioTempo = time.time()
    
    posicoes = buscaTabelaHash(linhas, valorBusca)

    fimTempo = time.time()

    # Exibe os resultados
    print(f"Minha ordenação Hash demorou {fimTempo - inicioTempo:.6f} segundos.")
    print(f"Nota: '{valorBusca}' \nPresente: {'Sim' if posicoes else 'Não'} \nQuantidade: {len(posicoes)} \nPosições: {posicoes}")

if __name__ == "__main__":
    main()

