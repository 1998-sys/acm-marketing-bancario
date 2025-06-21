# Análise de Correspondência Múltipla (ACM) e Segmentação de Clientes com K-Means

Este projeto tem como objetivo explorar dados de marketing bancário por meio da técnica de Análise de Correspondência Múltipla (ACM) e, posteriormente, aplicar o algoritmo de K-Means para identificar perfis de clientes.

## Objetivo

Analisar variáveis categóricas relacionadas a campanhas de marketing de uma instituição financeira, buscando identificar padrões de comportamento entre os clientes.

## Metodologia

### 1. Análise de Correspondência Múltipla (ACM)

A ACM foi aplicada para reduzir a dimensionalidade dos dados categóricos e possibilitar a visualização da relação entre categorias.

- **Número de variáveis:** 7  
- **Número total de categorias:** 35  
- **Número de dimensões resultantes:** 28  
- **Variância explicada pelas 2 primeiras dimensões:** 14,16%

🔎 **Observação:** A baixa variância explicada pelas primeiras dimensões dificultou a interpretação gráfica e a separação clara entre os perfis de clientes.

### 2. Agrupamento com K-Means

Como alternativa, aplicou-se o algoritmo K-Means utilizando as coordenadas das **observações** obtidas pela ACM.

- O número de clusters foi definido por meio do **método do cotovelo**, resultando em **20 grupos**.
- Em seguida, foi traçado um **perfil representativo para cada cluster**, com base nas categorias mais frequentes.


### Conclusão
Apesar da aplicação inicial da ACM não ter revelado separações claras entre os perfis devido à baixa variância explicada, a utilização do K-Means permitiu a segmentação dos clientes em grupos semelhantes, contribuindo para uma melhor compreensão dos padrões presentes no dataset.