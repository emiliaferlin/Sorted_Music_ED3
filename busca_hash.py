import re
import time
import os

def carregaTexto(texto):
    # Remove caracteres extras e mantém apenas letras e números
    linhas = texto.split("\n")
    dadosProcessados = [re.sub(r'[^a-zA-Z0-9]', '', linha.strip()) for linha in linhas if linha.strip()]
    return sorted(dadosProcessados)

def buscaTabelaHash(lista, valor):
    tabelaHash = {}
    for i, item in enumerate(lista):
        if item.startswith(valor):
            if valor not in tabelaHash:
                tabelaHash[valor] = []
            tabelaHash[valor].append(i)

    if valor in tabelaHash:
        return sorted(tabelaHash[valor])
    else:
        return []

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
    posicoes = buscaTabelaHash(dadosOrdenados, valorBusca)

    fimTempo = time.time()

    # Exibe os resultados
    print(f"Minha ordenação demorou {fimTempo - inicioTempo:.6f} segundos.")
    print(f"Nota: '{valorBusca}' \nPresente: {'Sim' if posicoes else 'Não'} \nQuantidade: {len(posicoes)} \nPosições: {posicoes}")

if __name__ == "__main__":
    main()
