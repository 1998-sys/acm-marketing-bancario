import pandas as pd
import seaborn as sns 
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from matplotlib import cm
import numpy as np
import warnings
warnings.filterwarnings("ignore")


#df=pd.read_csv('data/processed/bank_marketing_processed.csv')

def analise_univariada(data, variavel):
    """
     Análise univariada para variáveis categóricas
     :param data: Dataframe contendo os dados
     :param variavel: Nome da coluna a ser analisada
     :return: None

     Retorna uma tabela com a frequência
     Plota um gráfico com a frequência e exibe os valores
    """
    if variavel not in data.columns:
        print(f'A variável {variavel} não está presente no Dataframe.')

        

    # Tabela de frequência 
    tabela_frequencia = data[variavel].value_counts().reset_index()
    tabela_frequencia.columns = [variavel, 'Frequency']
    tabela_frequencia['Percent'] = (tabela_frequencia['Frequency'] / len(data) * 100).round(2)
    # linha total
    df_total = pd.DataFrame({
            variavel: 'Total',
            'Frequency': tabela_frequencia['Frequency'].sum(),
            'Percent': [100.0]

        })

    tabela_total = pd.concat([tabela_frequencia, df_total], ignore_index=True)

    print(f'Tabela de Frequencia {variavel}')
    display(tabela_total)

    # Aplica palleta de cores contínua
    valores = tabela_frequencia['Frequency'].values
    norm = (valores - valores.min())/(valores.max()- valores.min())

    cmap = cm.get_cmap('Blues')  # Use a colormap with 256 colors
    cores = [cmap(n) for n in norm]
    cores_hex = [rgb2hex(c[:3]) for c in cores]

    plt.figure(figsize=(7,5))
    ax = sns.barplot(x=variavel, y='Frequency', data=tabela_frequencia, palette=cores_hex)
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)
    for p in ax.patches:
        altura = p.get_height()
        cor_barra = p.get_facecolor()
  
        luminancia = 0.299 * cor_barra[0] + 0.587 * cor_barra[1] + 0.114 * cor_barra[2]
        cor_texto = 'black' if luminancia > 0.6 else 'white'
    
        ax.text(
            x=p.get_x() + p.get_width() / 2,
            y=altura / 2,
            s=f'{int(altura)}',
            ha='center',
            va='center',
            color=cor_texto,
            fontweight='bold',
            fontsize=8
        )
    plt.title(f'Frequency of {variavel}', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
    ax.set_xlabel('')
    ax.set_ylabel('')
    plt.show()

def label_point(x, y, val, ax):
    """
    Função que plota o nome das categorias no gráfico
    """
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'] + 0.03, point['y'] - 0.02, point['val'], fontsize=5)


def mapa_percptual(data,coord, tabela_autovalores):
    """
     Função que plota o mapa perceptual das categorias
     :param data: dataframe de dados
     :param coord: coordenadas padrão
     :param tabela_autovalores: tabela_autovalores
     :return: None

     Plota o gráfico de mapa perceptual das variáveis
    """
    chart= coord.reset_index()

    nome_categ=[]
    for col in data:
        nome_categ.append(data[col].sort_values(ascending=True).unique())
        categorias = pd.DataFrame(nome_categ).stack().reset_index()

    var_chart = pd.Series(chart['index'].str.split('-', expand=True).iloc[:,0])

    chart_df_mca = pd.DataFrame(
        {
        'categoria': chart['index'],
        'obs_x': chart[0],
        'obs_y': chart[1],
        'variavel': var_chart,
        'categoria_id': categorias[0]
            })
    

    label_point(x = chart_df_mca['obs_x'],
            y = chart_df_mca['obs_y'],
            val = chart_df_mca['categoria_id'],
            ax = plt.gca())
    
    sns.scatterplot(data=chart_df_mca, x='obs_x', y='obs_y', hue='variavel', s=20)
    sns.despine(top=True, right=True, left=False, bottom=False)
    plt.axhline(y=0, color='lightgrey', ls='--', linewidth=0.8)
    plt.axvline(x=0, color='lightgrey', ls='--', linewidth=0.8)
    plt.tick_params(size=2, labelsize=6)
    plt.legend(bbox_to_anchor=(1.25,-0.2), fancybox=True, shadow=True, ncols=10, fontsize='5')
    plt.title("Mapa Perceptual - MCA", fontsize=12)
    plt.xlabel(f"Dim. 1: {tabela_autovalores.iloc[0,1]} da inércia", fontsize=8)
    plt.ylabel(f"Dim. 2: {tabela_autovalores.iloc[1,1]} da inércia", fontsize=8)
    plt.show()








