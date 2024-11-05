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
        


caminho_lista = 'C:/Users/Mili/Desktop/songs4JSONvector.json'
caminho_linhas = 'C:/Users/Mili/Desktop/songs4LineByLine.json'

dados_lista = ler_arquivo_json(caminho_lista)
dados_linhas = ler_arquivo_json(caminho_linhas)

start_time_Guru99 = time.time()
# Ordenando a lista de dicionários pela chave 'arq' e 'ordem'
dados_ordenados = sorted(dados_lista, key=lambda x: (x['arq'], x['ordem']))

time.sleep(1)
end_time_Guru99 = time.time()
print("Tempo final do sorted de arquivo: ", end_time_Guru99 - start_time_Guru99)

start_time_Guru99 = time.time()
with open("dados_ordenados.txt", "w") as arquivo:
    arq_anterior = None  # Inicializa uma variável para o controle do 'arq' anterior
    
    for item in dados_ordenados:
        # Verifica se o 'arq' mudou
        if item['arq'] != arq_anterior:
            arquivo.write(f"\nArquivo {item['arq']}:\n")  # Imprime a mudança de arquivo
            arq_anterior = item['arq']  # Atualiza 'arq_anterior'

        arquivo.write(f"{item['notas']}\n")
        
time.sleep(1)
end_time_Guru99 = time.time()
print("Dados gravados em 'dados_ordenados.txt'")
print("Tempo final gravou: ", end_time_Guru99 - start_time_Guru99)
        
# Exibindo os dados
#for item in dados_ordenados:
    #print(item)
    
#for item in dados_linhas:
    #print(item)