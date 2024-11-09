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

# Ordenando dadosLista
# Função Radix Sort para ordenar pela chave 'ordem' e depois 'arq'
def countingSortRadix(arr, exp, key_func):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (key_func(arr[i]) // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (key_func(arr[i]) // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radixSort(arr, key_func):
    max_val = key_func(max(arr, key=key_func))
    exp = 1
    while max_val // exp > 0:
        countingSortRadix(arr, exp, key_func)
        exp *= 10

# Ordenando a lista de dicionários pela chave 'ordem' e depois 'arq' usando Radix Sort
dadosRadix = dadosLista.copy()
startTimeRadix = time.time()

# Primeiro, ordenamos pela chave 'ordem'
radixSort(dadosRadix, key_func=lambda x: x['ordem'])

# Depois, ordenamos pela chave 'arq' para manter a estabilidade
radixSort(dadosRadix, key_func=lambda x: x['arq'])

endTimeRadix = time.time()
print(f"Radix Sort demorou {endTimeRadix - startTimeRadix:.6f} segundos.")

### Double Sort (Dupla Ordenação) usando sorted()
startTimeSorted = time.time()
dadosOrdenados = sorted(dadosLista, key=lambda x: (x['arq'], x['ordem']))
endTimeSorted = time.time()
print(f"Sorted (dupla ordenação) demorou {endTimeSorted - startTimeSorted:.6f} segundos.")

# Função para gerar a chave de ordenação com base nas chaves 'arq' e 'ordem'
def chaveOrdenacao(item):
    return (item['arq'], item['ordem'])

### Quicksort
def quicksort(arr, low, high, key_func):
    if low < high:
        pi = partition(arr, low, high, key_func)
        quicksort(arr, low, pi - 1, key_func)
        quicksort(arr, pi + 1, high, key_func)

def partition(arr, low, high, key_func):
    pivot = key_func(arr[high])
    i = low - 1
    for j in range(low, high):
        if key_func(arr[j]) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

dadosQuicksort = dadosLista.copy()
startTimeQuicksort = time.time()
quicksort(dadosQuicksort, 0, len(dadosQuicksort) - 1, chaveOrdenacao)
endTimeQuicksort = time.time()
print(f"Quicksort demorou {endTimeQuicksort - startTimeQuicksort:.6f} segundos.")

### Heapsort
def heapsort(arr, key_func):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key_func)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key_func)

def heapify(arr, n, i, key_func):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and key_func(arr[l]) > key_func(arr[largest]):
        largest = l
    if r < n and key_func(arr[r]) > key_func(arr[largest]):
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key_func)

dadosHeapsort = dadosLista.copy()
startTimeHeapsort = time.time()
heapsort(dadosHeapsort, chaveOrdenacao)
endTimeHeapsort = time.time()
print(f"Heapsort demorou {endTimeHeapsort - startTimeHeapsort:.6f} segundos.")

def meuSort(arr, key):
    valorMax = max(arr, key=key)
    valorMin = min(arr, key=key)
    tamanhoElementos = key(valorMax) - key(valorMin) + 1

    # Array de contagem e array de saída para os elementos ordenados
    contador = [0] * tamanhoElementos
    saida = [None] * len(arr)

    # Contagem de cada elemento baseado na chave
    for elem in arr:
        contador[key(elem) - key(valorMin)] += 1

    # Acumulação para posição final dos elementos
    for i in range(1, len(contador)):
        contador[i] += contador[i - 1]

    # Ordena os elementos no array de saída
    for elem in reversed(arr):
        index = key(elem) - key(valorMin)
        saida[contador[index] - 1] = elem
        contador[index] -= 1

    return saida

startTime = time.time()
# Ordena pela chave 'ordem' primeiro
minhaOrdenacao = meuSort(dadosLista, key=lambda x: x["ordem"])
# Ordena pela chave 'arq' mantendo a estabilidade da ordem de 'ordem'
minhaOrdenacaoFinal = meuSort(minhaOrdenacao, key=lambda x: x["arq"])
endTime = time.time()
print(f"Minha ordenação manual demorou {endTime - startTime:.6f} segundos.")


startTimeLeitura = time.time()
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

# Fecha o último arquivo após o loop
if arquivo:
    arquivo.close()
        
endTimeLeitura = time.time()
print("Tempo final ao gravar dados: ", endTimeLeitura - startTimeLeitura)