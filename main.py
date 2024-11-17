import json
import time

def lerArquivoLista(caminhoArquivo):
    with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def lerArquivoLinha(caminhoArquivo):
    dados = []
    with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if linha.strip(): # Ignorar linhas vazias
                dados.append(json.loads(linha))
    return dados

def lerArquivoJson(caminhoArquivo):
    with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
        primeira_linha = arquivo.readline().strip()
        
        if primeira_linha.startswith('['):
            arquivo.seek(0)  # Retorna ao início do arquivo
            return lerArquivoLista(caminhoArquivo)
        else:  # JSON em linhas separadas
            arquivo.seek(0)
            return lerArquivoLinha(caminhoArquivo)
        

dadosLista = lerArquivoJson("songs4JSONvector.json")
dadosLinha = lerArquivoJson("songs4LineByLine.json")

def countingSort(arr, key):
    valorMax = max(arr, key=key)
    valorMin = min(arr, key=key)
    #aqui determina o numero de elemntos a serem trabalhados
    tamanhoElementos = key(valorMax) - key(valorMin) + 1

    # Array de contagem e array de saída para os elementos ordenados
    contador = [0] * tamanhoElementos
    saida = [None] * len(arr)

    # Contagem de cada elemento baseado na chave
    # Quantas vezes cada elemento (ajustado pela função key) ocorre em arr
    for elem in arr:
        contador[key(elem) - key(valorMin)] += 1

    # Acumulação para posição final dos elementos
    # Cada posição armazena a posição final de cada elemento
    for i in range(1, len(contador)):
        contador[i] += contador[i - 1]

    # Ordena os elementos no array de saída
    #Para cada elemento de arr (começando do último para manter a estabilidade), 
    # ele encontra a posição correta usando o índice acumulado e armazena o elemento em saida.
    #O contador para o índice é decrementado após cada uso, garantindo que os 
    # próximos elementos iguais sejam colocados na posição anterior.
    for elem in reversed(arr):
        index = key(elem) - key(valorMin)
        saida[contador[index] - 1] = elem
        contador[index] -= 1

    return saida

# Copia dos dados e mede o tempo de execução
startTime = time.time()
minhaOrdenacao = countingSort(dadosLista, key=lambda x: x["ordem"])
minhaOrdenacaoFinal = countingSort(minhaOrdenacao, key=lambda x: x["arq"])
endTime = time.time()
print(f"Minha ordenação demorou {endTime - startTime:.6f} segundos.")


arquivoAnterior = None 
arquivo = None
#Escreve o resultado em cada arquivo
for item in minhaOrdenacaoFinal:
    if item['arq'] != arquivoAnterior:
        if arquivo:
            arquivo.close()
        nome_arquivo = f"{item['arq']}.txt"
        arquivo = open(nome_arquivo, "w")
        arquivoAnterior = item['arq']
    arquivo.write(f"{item['notas']}\n")

if arquivo:
    arquivo.close()
        