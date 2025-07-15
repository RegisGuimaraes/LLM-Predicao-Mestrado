# LLM-Predicao-Mestrado

Este repositório contém os arquivos e dados relacionados a uma dissertação de mestrado sobre previsão de resultados financeiros utilizando Modelos de Linguagem Grandes (LLMs).

## Estrutura do Projeto

A seguir, uma descrição de como os recursos estão organizados neste repositório:

### `/` (Diretório Raiz)

Contém scripts principais para processamento e manipulação de dados.
- `remove_inconsistent_tickers.py`: Script para remover tickers de ações inconsistentes dos conjuntos de dados.
- `rename_previsoes_files.py`: Script utilizado para renomear e organizar os arquivos de previsões gerados pelo LLM.
- `README.md`: Este arquivo.

### `/Arquivos Previsoes/`

Este diretório armazena as saídas brutas e processadas das previsões do LLM.

- **`/Previsoes/`**: Contém os arquivos brutos gerados pelo modelo, incluindo:
    - `chain_of_thoughts_*`: Raciocínio detalhado do modelo para chegar a uma previsão.
    - `logs_*`: Logs de execução do processo de previsão.
    - `previsoes_primeiro_llm_*`: As previsões iniciais geradas.
    - `prompts_*`: Os prompts exatos que foram enviados ao modelo.
    *Os arquivos nesta pasta foram renomeados para um formato numérico sequencial para melhor organização.*

- **`/Previsoes Unificadas/`**: Contém arquivos de previsão agregados e consolidados em formatos como `.json` e `.txt`. Inclui os resultados finais após a limpeza e o processamento dos dados brutos.

### `/Baixados CVM/`

Armazena os dados financeiros oficiais baixados do portal de dados abertos da CVM (Comissão de Valores Mobiliários).

- **`dfp_cia_aberta_*`**: Contém as Demonstrações Financeiras Padronizadas (DFP) anuais, separadas por ano.
- **`itr_cia_aberta_*`**: Contém as Informações Trimestrais (ITR), também separadas por ano.

### `/Dados Para Otimizacao/`

Contém os conjuntos de dados preparados para serem utilizados em modelos de otimização de portfólio.

- `eps_yield_*_matrix.csv`: Matrizes de "Earnings Per Share Yield" (projetado, consenso e ingênuo).
- `prices_*.csv`: Dados de preços de ações, ajustados e não ajustados.
- `splits_events_*.csv`: Histórico de eventos de desdobramento (split/inplit) de ações.

### `/Dados Preco/`

Diretório destinado ao armazenamento de dados de preços (atualmente vazio).

### `/Graficos e CSV Otimizadores/`

Armazena os resultados gerados pelos modelos de otimização.

- **`/Charts/`**: Gráficos e visualizações.
- **`/CSV/`**: Arquivos CSV com os resultados das otimizações.