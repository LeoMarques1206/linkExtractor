import pandas as pd
import matplotlib.pyplot as plt
import os

# Função para ler os arquivos CSV
def read_csv_files(file_paths):
    dataframes = []
    for file in file_paths:
        df = pd.read_csv(file)
        
        # Verifique se a coluna 'Average Response Time' existe
        if 'Average Response Time' not in df.columns:
            print(f"Aviso: 'Average Response Time' não encontrado em {file}")
            continue  # Pular arquivos sem a coluna necessária
        
        # Adiciona uma coluna 'source' para identificar o tipo de arquivo (Ruby ou Python)
        if 'ruby' in file.lower():
            df['source'] = 'Ruby'
        elif 'python' in file.lower():
            df['source'] = 'Python'
        
        # Adiciona uma coluna para diferenciar se é com cache ou sem cache
        if 'cache' in file.lower():
            df['cache'] = 'Cache'
        else:
            df['cache'] = 'No Cache'
        
        # Extraindo o número de usuários do nome do arquivo
        # Aqui estamos assumindo que o nome do arquivo tem um padrão como python-10.csv ou ruby-cache-500.csv
        try:
            users = int(file.split('-')[-1].replace('.csv', ''))
            df['Users'] = users
        except ValueError:
            print(f"Erro ao extrair número de usuários de {file}")
            continue  # Ignorar arquivos com nomes inesperados
        
        dataframes.append(df)
    
    # Concatenate all dataframes into one
    return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

# Função para extrair a média de tempo de resposta
def get_average_response_time(df):
    return df['Average Response Time'].mean()

# Função para gerar gráficos
def plot_response_time(df, metric='Average Response Time'):
    # Verifica se o DataFrame não está vazio
    if df.empty:
        print("Nenhum dado disponível para plotar.")
        return

    # Calculando a média por grupo (Ruby/Python, Cache/No Cache, e número de usuários)
    grouped_df = df.groupby(['source', 'cache', 'Users']).agg({metric: 'mean'}).reset_index()
    
    # Criando os gráficos
    plt.figure(figsize=(10, 6))

    for source in grouped_df['source'].unique():
        source_df = grouped_df[grouped_df['source'] == source]
        for cache_type in source_df['cache'].unique():
            cache_df = source_df[source_df['cache'] == cache_type]
            plt.plot(cache_df['Users'], cache_df[metric], label=f'{source} - {cache_type}')

    plt.title(f'{metric} vs Número de Usuários')
    plt.xlabel('Número de Usuários')
    plt.ylabel(metric)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    directory = './csvs'
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

    # Lendo e concatenando os arquivos CSV
    df = read_csv_files(files)

    # Plotando o gráfico para a média do tempo de resposta
    plot_response_time(df, metric='Average Response Time')

if __name__ == "__main__":
    main()
