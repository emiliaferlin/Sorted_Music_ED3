import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from main import lerArquivoJson
dadosLista = lerArquivoJson("songs4JSONvector.json")

# Função para gerar a chave de ordenação com base nas chaves 'arq' e 'ordem'
def chaveOrdenacao(item):
    return (item['arq'], item['ordem'])

# Função HeapSort
def heapSort(arr, key_func):
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

# Copia dos dados e mede o tempo de execução
dadosHeapSort = dadosLista.copy()
startTimeHeapSort = time.time()
heapSort(dadosHeapSort, chaveOrdenacao)
endTimeHeapSort = time.time()
print(f"HeapSort demorou {endTimeHeapSort - startTimeHeapSort:.6f} segundos.")

# Função para escrever o resultado em arquivos separados por 'arq'
def escreve_ordenacao_arquivos(dados_ordenados):
    arquivo_anterior = None
    arquivo = None
    try:
        for item in dados_ordenados:
            if item['arq'] != arquivo_anterior:
                if arquivo:
                    arquivo.close()
                nome_arquivo = f"{item['arq']}heap.txt"
                arquivo = open(nome_arquivo, "w")
                arquivo_anterior = item['arq']
            arquivo.write(f"{item['notas']}\n")
    finally:
        if arquivo:
            arquivo.close()

escreve_ordenacao_arquivos(dadosHeapSort)
