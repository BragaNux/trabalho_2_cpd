# Mini-Steam: Classificação e Pesquisa de Jogos

## Sobre o Projeto
O **Mini-Steam** é um sistema de classificação e pesquisa de jogos para uma loja digital. Este projeto foi desenvolvido como parte de um trabalho acadêmico com o objetivo de implementar um mecanismo de busca eficiente para jogos baseado em preço e gênero, utilizando estruturas de dados como Árvore Binária de Busca (BST) e Hash Table.

O sistema permite que os usuários filtrem e busquem jogos com base em critérios como:
- Preço exato.
- Faixa de preço.
- Gêneros.
- Jogos gratuitos.

## Funcionalidades Implementadas
### 1. **Gerenciamento de Jogos por Preço (BST)**
- Implementação de uma **Árvore Binária de Busca (BST)** para classificar os jogos com base no preço.
- Funções:
  - Inserção de jogos na árvore com base no preço.
  - Busca por preço exato.
  - Busca por faixa de preços (intervalos).

### 2. **Gerenciamento de Jogos por Gênero (Hash Table)**
- Implementação de uma **Hash Table** para indexar jogos com base em seus gêneros.
- Funções:
  - Indexação de jogos por múltiplos gêneros.
  - Busca eficiente por gêneros.
  - Tratamento de colisões na tabela de hashing.

### 3. **Busca de Jogos por ID**
- Adição de um filtro para **buscar jogos por ID**.
- Quando o usuário fornece um ID, o sistema retorna apenas o jogo com esse ID específico.

### 4. **Interface Gráfica com Flask**
- Um front-end simples para interação com o sistema.
- Funcionalidades:
  - **Upload de arquivo**: Carrega um arquivo `.txt` com a lista de jogos.
  - **Filtros interativos**:
    - Preço exato.
    - Faixa de preço.
    - Gênero (dropdown dinâmico com os gêneros do arquivo).
    - Jogos gratuitos (checkbox).
    - Busca de jogos por ID.
  - **Aplicação dos filtros**: Exibe os jogos que atendem aos critérios definidos.
  - **Exportação**: Possibilidade de exportar os jogos filtrados para um arquivo `.csv`.

### 5. **Mensagens Informativas**
- Exibe mensagens de feedback para o usuário:
  - "Arquivo carregado com sucesso."
  - "Nenhum resultado encontrado com os filtros aplicados."
  - "Erro ao carregar o arquivo."

## Tecnologias Utilizadas
- **Linguagem**: Python 3.12
- **Framework**: Flask (para a interface web)
- **Estruturas de Dados**:
  - Árvore Binária de Busca (BST) para gerenciar jogos por preço.
  - Hash Table para gerenciar jogos por gênero.
- **Bootstrap**: Para estilização básica da interface.

## Como Rodar o Projeto

### 1. **Clone o Repositório**
Primeiro, clone o repositório para a sua máquina local:
```bash
git clone <url-do-repositorio>
cd <nome-da-pasta-do-projeto>
