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

# Armazenamento dos tempos de resposta de 95º percentil por linguagem, cache e número de usuários
percentil_95_por_combinacao = {}

# Processamento dos dados
for linguagem in linguagens:
    for cache in caches:
        percentil_95_por_combinacao[(linguagem, cache)] = []
        for n_usuarios in num_usuarios:
            # Nome do arquivo de acordo com a combinação de linguagem, cache e número de usuários
            filename = f"{linguagem} - {cache} - {n_usuarios}.csv"
            file_path = os.path.join(data_path, filename)
            
            if os.path.isfile(file_path):
                data = pd.read_csv(file_path)
                # Cálculo do 95º percentil do tempo de resposta
                percentil_95 = data["95%"].mean()  # Supondo que "95%" é a coluna no CSV com o valor do percentil 95
                percentil_95_por_combinacao[(linguagem, cache)].append(percentil_95)
            else:
                print(f"Arquivo {filename} não encontrado.")
                percentil_95_por_combinacao[(linguagem, cache)].append(None)

# Geração dos gráficos
fig, ax = plt.subplots(figsize=(10, 6))

# Preparação para plotar as barras
width = 0.2  # Largura das barras
x = np.arange(len(num_usuarios))  # Posições para os números de usuários

# Plotando as barras para cada combinação de linguagem e cache
for i, (linguagem, cache) in enumerate(percentil_95_por_combinacao.keys()):
    percentis = percentil_95_por_combinacao[(linguagem, cache)]
    ax.bar(x + i * width, percentis, width, label=f"{linguagem.capitalize()} - {cache}")

# Ajustes do gráfico
ax.set_xlabel("Número de Usuários")
ax.set_ylabel("95º Percentil do Tempo de Resposta (ms)")
ax.set_title("95º Percentil do Tempo de Resposta por Número de Usuários, Linguagem e Cache")
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(num_usuarios)
ax.legend(title="Configuração")
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Salva o gráfico gerado
plt.savefig("grafico_percentil_95.png")
plt.close(fig)
