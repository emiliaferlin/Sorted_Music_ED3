import sys
import os
import time

# Adiciona o diretório raiz (Sorted_Music_ED3) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Agora você pode importar as funções do main.py
from main import lerArquivoJson

# Carregar dados usando a função de main.py
dadosLista = lerArquivoJson("songs4JSONvector.json")

# Função de contagem para um dígito específico (usada pelo Radix Sort)
def countingSortExp(arr, exp, key_func):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Conta a ocorrência dos dígitos
    for i in range(n):
        index = (key_func(arr[i]) // exp) % 10
        count[index] += 1

    # Atualiza as posições de contagem para criar a posição de cada elemento
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Constroi o array de saída
    i = n - 1
    while i >= 0:
        index = (key_func(arr[i]) // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copia o resultado ordenado para o array original
    for i in range(n):
        arr[i] = output[i]

# Função Radix Sort principal para múltiplos dígitos
def radixSort(arr, key_func):
    # Encontra o valor máximo para saber o número de dígitos
    max_val = key_func(max(arr, key=key_func))
    exp = 1
    while max_val // exp > 0:
        countingSortExp(arr, exp, key_func)
        exp *= 10

# Cria uma cópia dos dados para ordenar com o Radix Sort
dadosRadix = dadosLista.copy()

# Medição do tempo de execução do Radix Sort
startTimeRadix = time.time()
# Primeira ordenação pela chave 'ordem' (valor numérico)
radixSort(dadosRadix, key_func=lambda x: x['ordem'])
# Ordena por 'arq' para manter a estabilidade (usando outro método, pois 'arq' não é numérico)
dadosRadix.sort(key=lambda x: x['arq'])
endTimeRadix = time.time()
print(f"Radix Sort demorou {endTimeRadix - startTimeRadix:.6f} segundos.")

# Função para escrever o resultado em arquivos separados por 'arq'
def escreve_ordenacao_arquivos(dados_ordenados):
    arquivo_anterior = None
    arquivo = None
    try:
        for item in dados_ordenados:
            if item['arq'] != arquivo_anterior:
                if arquivo:
                    arquivo.close() 
                nome_arquivo = f"{item['arq']}radix.txt"
                arquivo = open(nome_arquivo, "w")
                arquivo_anterior = item['arq']
            arquivo.write(f"{item['notas']}\n") 
    finally:
        if arquivo:
            arquivo.close()

escreve_ordenacao_arquivos(dadosRadix)
