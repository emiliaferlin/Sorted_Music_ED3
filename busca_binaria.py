import re
import time
import os

# Função para processar e ordenar os dados
def carregaTexto(texto):
    linhas = texto.split("\n")
    return sorted([re.sub(r'[^a-zA-Z0-9]', '', linha.strip()) for linha in linhas if linha.strip()])

# Função de busca binária
def buscaBinaria(lista, valor):
    inicio, fim = 0, len(lista) - 1
    posicoes = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio].startswith(valor):
            # Encontra todas as ocorrências
            posicoes.append(meio)
            i = meio - 1
            while i >= 0 and lista[i].startswith(valor):
                posicoes.append(i)
                i -= 1
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
    valorBusca = input("Digite a nota que deseja encontrar: ").strip()
    
    if not valorBusca:
        print("Erro: Nenhum valor foi inserido. Por favor, tente novamente.")
        exit()

    # Processa o arquivo e realiza a busca
    with open('52.txt', 'r') as file:
        arquivo = file.read()

    inicioTempo = time.time()

    dadosOrdenados = carregaTexto(arquivo)
    buscaEncontrada = buscaBinaria(dadosOrdenados, valorBusca)

    fimTempo = time.time()

    # Exibe os resultados
    print(f"Minha ordenação demorou {fimTempo - inicioTempo:.6f} segundos.")
    print(f"Nota: '{valorBusca}' \nPresente: {'Sim' if buscaEncontrada else 'Não'} \nQuantidade: {len(buscaEncontrada)} \nPosições: {buscaEncontrada}")

if __name__ == "__main__":
    main()

