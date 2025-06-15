import pandas as pd

df_banking = pd.read_csv('data/raw/bank_marketing_dataset.csv')

# Redução para as colunas relevantes
df_banking = df_banking[['age', 'job', 'marital', 'education', 'default', 'housing', 'loan']]


# Categorização da coluna idade

def classificação_idade(idade):
    """
    Classifica a idade em categorias
    """
    if idade < 18:
        return 'young'
    elif 18 <= idade <=29:
        return 'young adult'
    elif 30 <= idade <= 59:
        return 'Adult'
    else:
        return 'Elderly'


# Aplicando a função de classificação em Age
df_banking['age'] = df_banking['age'].apply(classificação_idade)

# Ajustando as categorias da coluna 'Education'
df_banking['education']= df_banking['education'].str.replace('.',' ', regex=False)
# Ajustando a categoria 'basic' da coluna 'Education'
df_banking['education'] = df_banking['education'].str.replace(r'^(basic)\s.*', r'\1', regex=True)


# Salvando o DataFrame Tratado
df_banking.to_csv('data/processed/bank_marketing_processed.csv', index=False)
