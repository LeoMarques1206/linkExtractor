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

# Armazenamento dos tempos de resposta médio por linguagem, cache e número de usuários
tempo_resposta_por_combinacao = {}

# Processamento dos dados
for linguagem in linguagens:
    for cache in caches:
        tempo_resposta_por_combinacao[(linguagem, cache)] = []
        for n_usuarios in num_usuarios:
            # Nome do arquivo de acordo com a combinação de linguagem, cache e número de usuários
            filename = f"{linguagem} - {cache} - {n_usuarios}.csv"
            file_path = os.path.join(data_path, filename)
            
            if os.path.isfile(file_path):
                data = pd.read_csv(file_path)
                # Média de tempo de resposta
                media_resposta = data["Average Response Time"].mean()
                tempo_resposta_por_combinacao[(linguagem, cache)].append(media_resposta)
            else:
                print(f"Arquivo {filename} não encontrado.")
                tempo_resposta_por_combinacao[(linguagem, cache)].append(None)

# Geração dos gráficos
fig, ax = plt.subplots(figsize=(10, 6))

# Preparação para plotar as barras
width = 0.2  # Largura das barras
x = np.arange(len(num_usuarios))  # Posições para os números de usuários

# Plotando as barras para cada combinação de linguagem e cache
for i, (linguagem, cache) in enumerate(tempo_resposta_por_combinacao.keys()):
    tempos = tempo_resposta_por_combinacao[(linguagem, cache)]
    ax.bar(x + i * width, tempos, width, label=f"{linguagem.capitalize()} - {cache}")

# Ajustes do gráfico
ax.set_xlabel("Número de Usuários")
ax.set_ylabel("Tempo de Resposta Médio (s)")
ax.set_title("Tempo de Resposta Médio por Número de Usuários, Linguagem e Cache")
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(num_usuarios)
ax.legend(title="Configuração")
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Salva o gráfico gerado
plt.savefig("grafico_tempo_resposta.png")
plt.close(fig)
