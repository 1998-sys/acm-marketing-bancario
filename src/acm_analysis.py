import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import statsmodels.api as sm
import matplotlib.pyplot as plt
import prince
from itertools import combinations
from IPython.display import display
import seaborn as sns



def chi2(df):
    """
    Cria todas as tabelas de contingência possíveis entre as variáveis categóricas do DataFrame e imprime os resultados do teste qui-quadrado.
    :param df: DataFrame contendo os dados
    :return: None
    
    """
    for item in list(combinations(df.columns, 2)):
        print(f'Teste qui-quadrado entre {item[0]} e {item[1]}')
        tabela_contingencia = pd.crosstab(df[item[0]], df[item[1]])

        chi2, pvalor, gl, freq_esp = chi2_contingency(tabela_contingencia)
        print(f'Estatística qui-quadrado: {chi2}')
        print(f'p-valor da estatística: {round(pvalor,4)}')
        print(f'Graus de liberdade: {gl}', '\n')


def mca(df, components=2):
    """"
    Realiza A Análise de Correspondência Múltipla (MCA) em um Dataframe e plota o resultados.
    :param df: Dataframe contendo as variáveis categóricas
    :param components: Número de dimensões a serem consideradas na MCA (padrão 2)
    :return: coord_padrao: coordenadas padrão cálculadas
    :return: coord_obs: coordenadas da observação calculadas
    """
    mca = prince.MCA(n_components=components).fit(df)
    qtd_dimensoes = mca.J_ - mca.K_
    tabela_autovalores = mca.eigenvalues_summary

    print(f'Número de dimensões: {qtd_dimensoes}')
    print(f'Quantidade de Variáveis: {mca.K_}')
    print(f'Quantidade Total de Categorias: {mca.J_}')

    print(tabela_autovalores)

    print(mca.total_inertia_)

    coord_padrao = mca.column_coordinates(df)/np.sqrt(mca.eigenvalues_)

    coord_obs = mca.row_coordinates(df)

    return coord_padrao, coord_obs, tabela_autovalores






    

    


    

