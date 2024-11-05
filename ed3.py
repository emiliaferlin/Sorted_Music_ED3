import json
import time

def ler_arquivo_lista(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def ler_arquivo_linhas(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if linha.strip(): # Ignorar linhas vazias
                dados.append(json.loads(linha))
    return dados

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        primeira_linha = arquivo.readline().strip()
        
        if primeira_linha.startswith('['):
            arquivo.seek(0)  # Retorna ao início do arquivo
            return ler_arquivo_lista(caminho_arquivo)
        else:  # JSON em linhas separadas
            arquivo.seek(0)
            return ler_arquivo_linhas(caminho_arquivo)
        


caminho_lista = 'songs4JSONvector.json'
caminho_linhas = 'songs4LineByLine.json'

dados_lista = ler_arquivo_json(caminho_lista)
dados_linhas = ler_arquivo_json(caminho_linhas)
# Ordenando a lista de dicionários pela chave 'arq' e 'ordem'

### Double Sort (Dupla Ordenação) usando sorted()
start_time_sorted = time.time()
dados_ordenados = sorted(dados_lista, key=lambda x: (x['arq'], x['ordem']))
end_time_sorted = time.time()
print(f"Sorted (dupla ordenação) demorou {end_time_sorted - start_time_sorted:.6f} segundos.")

# Função para gerar a chave de ordenação com base nas chaves 'arq' e 'ordem'
def chave_ordenacao(item):
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

# Executando o Quicksort
dados_quicksort = dados_lista.copy()
start_time_quicksort = time.time()
quicksort(dados_quicksort, 0, len(dados_quicksort) - 1, chave_ordenacao)
end_time_quicksort = time.time()
print(f"Quicksort demorou {end_time_quicksort - start_time_quicksort:.6f} segundos.")

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

# Executando o Heapsort
dados_heapsort = dados_lista.copy()
start_time_heapsort = time.time()
heapsort(dados_heapsort, chave_ordenacao)
end_time_heapsort = time.time()
print(f"Heapsort demorou {end_time_heapsort - start_time_heapsort:.6f} segundos.")

start_time_Guru99 = time.time()
arq_anterior = None  # Inicializa uma variável para o controle do 'arq' anterior
arquivo = None  # Inicializa a variável do arquivo para que possa ser fechado corretamente

for item in dados_ordenados:
    # Verifica se o 'arq' mudou
    if item['arq'] != arq_anterior:
        # Fecha o arquivo anterior, se houver
        if arquivo:
            arquivo.close()
        
        # Abre um novo arquivo com o nome baseado em 'arq'
        nome_arquivo = f"{item['arq']}.txt"
        arquivo = open(nome_arquivo, "w")
        arq_anterior = item['arq']

    # Escreve as notas no arquivo atual
    arquivo.write(f"{item['notas']}\n")

# Fecha o último arquivo após o loop
if arquivo:
    arquivo.close()
        
end_time_Guru99 = time.time()
print("Tempo final ao gravar dados: ", end_time_Guru99 - start_time_Guru99)