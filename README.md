# Projeto de Índice Hash Estático

Este projeto implementa um sistema de índice hash estático com uma interface gráfica para ilustrar as operações sobre as estruturas de dados. O sistema permite a construção de um índice a partir de um arquivo de dados, busca de tuplas usando o índice, execução de um table scan e visualização de estatísticas relacionadas ao índice.

## Funcionalidades

- **Carregamento de Dados**: Carrega palavras a partir de um arquivo texto para a memória.
- **Construção do Índice**: Constrói um índice hash estático a partir das palavras carregadas.
- **Busca**: Permite buscar uma tupla específica usando a chave de busca.
- **Table Scan**: Realiza um table scan exibindo um número especificado de tuplas.
- **Estatísticas**: Mostra estatísticas como a taxa de colisões e overflows.

## Estruturas de Dados

- **Tupla**: Representa uma linha da tabela, contendo a chave de busca e os dados associados.
- **Página**: Representa a divisão e alocação física da tabela na mídia de armazenamento.
- **Bucket**: Mapeia chaves de busca em endereços de páginas, implementando a resolução de colisões.
- **Tabela**: Contém todas as tuplas e gerencia sua organização em páginas e buckets.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Interface Gráfica**: Tkinter

## Como Executar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de que o Python está instalado em seu sistema.
3. Navegue até a pasta raiz do projeto e execute o seguinte comando para iniciar a aplicação:

    ```bash
    python src/main.py
    ```

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contribuições

Contribuições são bem-vindas. Por favor, abra um issue para discutir as mudanças desejadas ou submeta um Pull Request.

## Autores

- João Pedro Rodrigues Tenório

## Agradecimentos

- Agradeça a qualquer pessoa ou recurso que tenha sido crucial para a realização do projeto.