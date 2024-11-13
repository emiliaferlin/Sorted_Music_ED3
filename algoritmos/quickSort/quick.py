import sys
import os
import time

# Adiciona o diretório raiz (Sorted_Music_ED3) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Agora você pode importar as funções do main.py
from main import lerArquivoJson

# Carregar dados usando a função de main.py
dadosLista = lerArquivoJson("songs4JSONvector.json")

# Função para gerar a chave de ordenação com base nas chaves 'arq' e 'ordem'
def chaveOrdenacao(item):
    return (item['arq'], item['ordem'])

### Implementação do QuickSort
def quickSort(arr, low, high, key_func):
    if low < high:
        pi = partition(arr, low, high, key_func)
        quickSort(arr, low, pi - 1, key_func)
        quickSort(arr, pi + 1, high, key_func)

def partition(arr, low, high, key_func):
    pivot = key_func(arr[high])
    i = low - 1
    for j in range(low, high):
        if key_func(arr[j]) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Copia dos dados e mede o tempo de execução
dadosQuickSort = dadosLista.copy()
startTimeQuickSort = time.time()
quickSort(dadosQuickSort, 0, len(dadosQuickSort) - 1, chaveOrdenacao)
endTimeQuickSort = time.time()
print(f"QuickSort demorou {endTimeQuickSort - startTimeQuickSort:.6f} segundos.")

# Escreve o resultado em arquivos
arquivoAnterior = None
arquivo = None

for item in dadosQuickSort:
    if item['arq'] != arquivoAnterior:
        if arquivo:
            arquivo.close()
        nome_arquivo = f"{item['arq']}quick.txt"
        arquivo = open(nome_arquivo, "w")
        arquivoAnterior = item['arq']
    arquivo.write(f"{item['notas']}\n")

if arquivo:
    arquivo.close()
