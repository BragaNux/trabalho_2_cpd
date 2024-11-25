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

### 3. **Interface Gráfica com Flask**
- Um front-end simples para interação com o sistema.
- Funcionalidades:
  - **Upload de arquivo**: Carrega um arquivo `.txt` com a lista de jogos.
  - **Filtros interativos**:
    - Preço exato.
    - Faixa de preço.
    - Gênero (dropdown dinâmico com os gêneros do arquivo).
    - Jogos gratuitos (checkbox).
  - **Aplicação dos filtros**: Exibe os jogos que atendem aos critérios definidos.
  - **Exportação**: Possibilidade de exportar os jogos filtrados para um arquivo `.csv`.

### 4. **Mensagens Informativas**
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
```bash
git clone <url-do-repositorio>
cd <nome-da-pasta-do-projeto>
```

### 2. **Crie um Ambiente Virtual**
Crie e ative um ambiente virtual para instalar as dependências do projeto:
```bash
python -m venv venv
```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. **Instale as Dependências**
```bash
pip install -r requirements.txt
```

### 4. **Execute o Projeto**
Inicie o servidor Flask:
```bash
python TrabalhoG2.py
```

Acesse o sistema no navegador:
```
http://127.0.0.1:5000/
```

### 5. **Fluxo de Uso**
1. **Envie o arquivo `.txt`**:
   - Faça o upload de um arquivo no formato:
     ```plaintext
     ID,Título,Desenvolvedor,Preço,Gêneros
     1,The Witcher 3,CD Projekt Red,150,RPG,Ação
     2,Stardew Valley,ConcernedApe,40,Indie,Simulação
     ```
2. **Aplique Filtros**:
   - Escolha os critérios desejados:
     - Preço exato.
     - Faixa de preço.
     - Gênero.
     - Jogos gratuitos.
   - Clique em "Carregar com Filtros".
3. **Visualize os Resultados**:
   - Os jogos que atendem aos filtros serão exibidos em uma tabela.
4. **Exporte os Resultados**:
   - Clique no botão "Exportar" para salvar os jogos filtrados em um arquivo `.csv`.

## Estrutura do Projeto
```
<nome-do-projeto>/
|— TrabalhoG2.py       # Arquivo principal do Flask
|— requirements.txt    # Dependências do projeto
|— templates/          # Páginas HTML (index.html)
|— uploads/            # Pasta para armazenar arquivos enviados
|— exports/            # Pasta para exportações de jogos filtrados
```

## Exemplo de Arquivo `.txt`
```plaintext
1,The Witcher 3,CD Projekt Red,150,RPG,Ação
2,Stardew Valley,ConcernedApe,40,Indie,Simulação
3,Doom Eternal,id Software,200,Ação,Tiro
4,Celeste,Maddy Makes Games,50,Indie,Plataforma
5,Cyberpunk 2077,CD Projekt Red,180,RPG,Ação
```

## O que foi Implementado
- **BST**: Gerenciamento e busca por preço.
- **Hash Table**: Gerenciamento e busca por gênero.
- **Interface Gráfica**: Upload de arquivos, aplicação de filtros e exibição de resultados.
- **Exportação**: Geração de arquivo `.csv` com os jogos filtrados.
- **Mensagens informativas**: Feedback ao usuário em caso de erro ou sucesso.

## Considerações Finais
O projeto foi desenvolvido com foco em soluções eficientes, integrando estruturas de dados para oferecer buscas rápidas e precisas. A interface gráfica torna o sistema mais acessível e permite uma experiência interativa para os usuários.

Qualquer sugestão de melhoria é bem-vinda. Obrigado por utilizar o Mini-Steam! 🚀

