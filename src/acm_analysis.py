import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import statsmodels.api as sm
import matplotlib.pyplot as plt
import prince
from itertools import combinations
from IPython.display import display



def tab_contingencia(df):
    """
    Cria e imprime todas as tabelas de contingência possíveis entre as variáveis categóricas do DataFrame
    :param df: DataFrame contendo os dados
    :return: None
    
    """
    for item in list(combinations(df.columns, 2)):
        print(f'Tabela de Contingência entre {item[0]} e {item[1]}')
        tabela_contingencia = pd.crosstab(df[item[0]], df[item[1]])

        #display(tabela_contingencia)

        chi2, pvalor, gl, freq_esp = chi2_contingency(tabela_contingencia)
        print(f'Estatística qui-quadrado: {chi2}')
        print(f'p-valor da estatística: {round(pvalor,4)}','\n')



