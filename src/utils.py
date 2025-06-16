import pandas as pd
import seaborn as sns 
from IPython.display import display



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
    tabela_frequencia.columns = [variavel, 'Frequencia']
    tabela_frequencia['Percent'] = (tabela_frequencia['Frequencia'] / len(data) * 100).round(2)
    # linha total
    df_total = pd.DataFrame({
            variavel: 'Total',
            'Frequencia': tabela_frequencia['Frequencia'].sum(),
            'Percent': [100.0]

        })

    tabela_frequencia = pd.concat([tabela_frequencia, df_total], ignore_index=True)

    print(f'Tabela de Frequencia {variavel}')
    display(tabela_frequencia)

    # Gráfico com a frequência
    sns.barplot(x=variavel, y='Frequencia', data=tabela_frequencia[:-1])










