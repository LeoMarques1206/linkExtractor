import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Caminho para os dados CSV
data_path = './csvs'

# Número de usuários para os testes
num_usuarios = [10, 500, 1000]

# Configurações para as linguagens e tipos de cache
linguagens = ['python', 'ruby']
caches = ['cache', 'NOcache']

# Armazenamento do número total de requisições por linguagem, cache e número de usuários
requisicoes_por_combinacao = {}

# Processamento dos dados
for linguagem in linguagens:
    for cache in caches:
        requisicoes_por_combinacao[(linguagem, cache)] = []
        for n_usuarios in num_usuarios:
            # Nome do arquivo de acordo com a combinação de linguagem, cache e número de usuários
            filename = f"{linguagem} - {cache} - {n_usuarios}.csv"
            file_path = os.path.join(data_path, filename)
            
            if os.path.isfile(file_path):
                data = pd.read_csv(file_path)
                # Cálculo do número total de requisições
                total_requisicoes = data["Request Count"].sum()
                requisicoes_por_combinacao[(linguagem, cache)].append(total_requisicoes)
            else:
                print(f"Arquivo {filename} não encontrado.")
                requisicoes_por_combinacao[(linguagem, cache)].append(None)

# Geração dos gráficos
fig, ax = plt.subplots(figsize=(10, 6))

# Preparação para plotar as barras
width = 0.2  # Largura das barras
x = np.arange(len(num_usuarios))  # Posições para os números de usuários

# Plotando as barras para cada combinação de linguagem e cache
for i, (linguagem, cache) in enumerate(requisicoes_por_combinacao.keys()):
    requisicoes = requisicoes_por_combinacao[(linguagem, cache)]
    ax.bar(x + i * width, requisicoes, width, label=f"{linguagem.capitalize()} - {cache}")

# Ajustes do gráfico
ax.set_xlabel("Número de Usuários")
ax.set_ylabel("Número Total de Requisições")
ax.set_title("Número Total de Requisições por Número de Usuários, Linguagem e Cache")
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(num_usuarios)
ax.legend(title="Configuração")
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Salva o gráfico gerado
plt.savefig("grafico_numero_requisicoes.png")
plt.close(fig)
