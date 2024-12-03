import time

# Função de busca binária
def buscaBinaria(lista, valor):
    inicio = 0 
    fim = len(lista) - 1
    posicoes = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        # Verificar se uma string começa com um determinado prefixo ou sequência do valor.
        if lista[meio].startswith(valor):
            # Encontra todas as ocorrências e adiciona no array de posicoes
            posicoes.append(meio)
            # Busca ocorrências anteriores ao meio - indices menores
            i = meio - 1
            while i >= 0 and lista[i].startswith(valor):
                posicoes.append(i)
                i -= 1
            # Busca ocorrências posteriores ao meio - indices maiores
            i = meio + 1
            while i < len(lista) and lista[i].startswith(valor):
                posicoes.append(i)
                i += 1
            break
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return sorted(posicoes)


def main():
    #%%MIDI program teste
    valorBusca = input("Digite a nota que deseja encontrar: ").strip()
    if not valorBusca:
        print("Erro: Nenhum valor foi inserido. Por favor, tente novamente.")
        return

    # Processa o arquivo e realiza a busca por linha
    with open('52.txt', 'r') as file:
        linhas = file.readlines()  # Lê cada linha do arquivo como um item de lista

    # Ordena a lista para busca binária
    valoresOrdenados = sorted(linhas)

    inicioTempo = time.time()
    
    posicoes = buscaBinaria(valoresOrdenados, valorBusca)

    fimTempo = time.time()

    # Exibe os resultados
    print(f"Minha busca binária demorou {fimTempo - inicioTempo:.6f} segundos.")
    print(f"Nota: '{valorBusca}' \nPresente: {'Sim' if posicoes else 'Não'} \nQuantidade: {len(posicoes)} \nPosições: {posicoes}")

if __name__ == "__main__":
    main()
