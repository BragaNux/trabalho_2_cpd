from flask import Flask, render_template, request, redirect, flash
import os

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash_messages'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Classe que representa um Jogo
class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos

# Classe para nó da Árvore Binária de Busca (BST)
class BSTNode:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

# Árvore Binária de Busca (BST)
class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        if self.raiz is None:
            self.raiz = BSTNode(jogo)
        else:
            self._inserir_recursivo(self.raiz, jogo)

    def _inserir_recursivo(self, no, jogo):
        if jogo.preco < no.jogo.preco:
            if no.esquerda is None:
                no.esquerda = BSTNode(jogo)
            else:
                self._inserir_recursivo(no.esquerda, jogo)
        else:
            if no.direita is None:
                no.direita = BSTNode(jogo)
            else:
                self._inserir_recursivo(no.direita, jogo)

    def buscar_todos(self):
        jogos = []
        self._inorder_traversal(self.raiz, jogos)
        return jogos

    def _inorder_traversal(self, no, jogos):
        if no:
            self._inorder_traversal(no.esquerda, jogos)
            jogos.append(no.jogo)
            self._inorder_traversal(no.direita, jogos)

# Classe para a Tabela de Hash
class HashTable:
    def __init__(self, tamanho=100):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return chave % self.tamanho

    def inserir(self, jogo):
        chave = self._hash(jogo.jogo_id)
        self.tabela[chave].append(jogo)

    def buscar(self, jogo_id):
        chave = self._hash(jogo_id)
        for jogo in self.tabela[chave]:
            if jogo.jogo_id == jogo_id:
                return jogo
        return None

# Motor de Busca de Jogos
class MotorBuscaJogos:
    def __init__(self):
        self.bst = BST()
        self.hash_table = HashTable()

    def carregar_jogos_de_arquivo(self, arquivo_caminho):
        try:
            with open(arquivo_caminho, 'r', encoding='utf-8') as file:
                self.bst = BST()  # Resetando a árvore
                self.hash_table = HashTable()  # Resetando a tabela de hash
                for linha in file:
                    dados = linha.strip().split(",")
                    jogo_id = int(dados[0])
                    titulo = dados[1]
                    desenvolvedor = dados[2]
                    preco = float(dados[3].replace(",", "."))
                    generos = dados[4:]
                    jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
                    self.bst.inserir(jogo)
                    self.hash_table.inserir(jogo)
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")

    def buscar_por_id(self, jogo_id):
        return self.hash_table.buscar(jogo_id)

    def buscar_todos(self):
        return self.bst.buscar_todos()

    def buscar_por_preco(self, preco):
        return [jogo for jogo in self.bst.buscar_todos() if jogo.preco == preco]

    def buscar_por_faixa_preco(self, preco_min, preco_max):
        return [jogo for jogo in self.bst.buscar_todos() if preco_min <= jogo.preco <= preco_max]

    def buscar_por_genero(self, genero):
        return [jogo for jogo in self.bst.buscar_todos() if genero in jogo.generos]

    def buscar_gratis(self):
        return [jogo for jogo in self.bst.buscar_todos() if jogo.preco == 0]

    def obter_generos_unicos(self):
        generos = set()
        for jogo in self.bst.buscar_todos():
            generos.update(jogo.generos)
        return sorted(generos)


motor_busca = MotorBuscaJogos()

@app.route("/", methods=["GET", "POST"])
def index():
    filtros_visiveis = False
    jogos = []
    generos_disponiveis = []
    jogo_encontrado = None

    if request.method == "POST" and 'upload' in request.form:
        file = request.files['file']
        if file.filename == '':
            flash("Nenhum arquivo selecionado!", "danger")
            return redirect("/")
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            motor_busca.carregar_jogos_de_arquivo(filepath)
            flash("Arquivo carregado com sucesso!", "success")
            filtros_visiveis = True
            generos_disponiveis = motor_busca.obter_generos_unicos()

    # Processamento do filtro por ID
    if request.method == "POST" and 'jogo_id' in request.form:
        jogo_id = request.form.get("jogo_id")
        if jogo_id:
            jogo_encontrado = motor_busca.buscar_por_id(int(jogo_id))
            if jogo_encontrado is None:
                flash("Jogo não encontrado pelo ID informado!", "warning")
            else:
                jogos = [jogo_encontrado]  # Aqui, atribuímos o jogo encontrado diretamente à variável jogos

    # Processamento de outros filtros
    if request.method == "POST" and 'filtrar' in request.form:
        preco_exato = request.form.get("preco_exato")
        preco_min = request.form.get("preco_min")
        preco_max = request.form.get("preco_max")
        genero = request.form.get("genero")
        apenas_gratis = request.form.get("gratis") == "on"
        filtros_visiveis = True
        generos_disponiveis = motor_busca.obter_generos_unicos()

        jogos = motor_busca.buscar_todos()
        if preco_exato:
            preco_exato = float(preco_exato.replace(",", "."))
            jogos = [jogo for jogo in jogos if jogo.preco == preco_exato]
        if preco_min and preco_max:
            preco_min = float(preco_min.replace(",", "."))
            preco_max = float(preco_max.replace(",", "."))
            jogos = [jogo for jogo in jogos if preco_min <= jogo.preco <= preco_max]
        if genero:
            jogos = [jogo for jogo in jogos if genero in jogo.generos]
        if apenas_gratis:
            jogos = [jogo for jogo in jogos if jogo.preco == 0]

        if not jogos:
            flash("Nenhum resultado encontrado com os filtros aplicados!", "warning")

    else:
        jogos = motor_busca.buscar_todos()

    # Ordenação
    ordenar = request.args.get('ordenar')
    if ordenar:
        if ordenar == "id":
            jogos = sorted(jogos, key=lambda x: x.jogo_id)
        elif ordenar == "titulo":
            jogos = sorted(jogos, key=lambda x: x.titulo)
        elif ordenar == "desenvolvedor":
            jogos = sorted(jogos, key=lambda x: x.desenvolvedor)
        elif ordenar == "preco":
            jogos = sorted(jogos, key=lambda x: x.preco)
        elif ordenar == "genero":
            jogos = sorted(jogos, key=lambda x: ', '.join(x.generos))

    return render_template("index.html", filtros_visiveis=filtros_visiveis, jogos=jogos,
                           generos=generos_disponiveis, jogo_encontrado=jogo_encontrado)

@app.route("/graficos/ordenar", methods=["POST"])
def graficos_ordenar():
    criterio = request.form.get("criterio")
    jogos = motor_busca.buscar_todos()

    if criterio == "preco_desc":
        jogos = sorted(jogos, key=lambda x: x.preco, reverse=True)
    elif criterio == "rpg_alfabetico":
        jogos = [jogo for jogo in jogos if "RPG" in jogo.generos]
        jogos = sorted(jogos, key=lambda x: x.titulo)
    elif criterio == "nome_alfabetico":
        jogos = sorted(jogos, key=lambda x: x.titulo)
    elif criterio == "desenvolvedor_alfabetico":
        jogos = sorted(jogos, key=lambda x: x.desenvolvedor)

    titulos = [jogo.titulo for jogo in jogos]
    precos = [jogo.preco for jogo in jogos]
    desenvolvedores = [jogo.desenvolvedor for jogo in jogos]

    return render_template(
        "graficos.html",
        titulos=titulos,
        precos=precos,
        desenvolvedores=desenvolvedores
    )

@app.route("/graficos", methods=["POST"])
def graficos():
    jogos = motor_busca.buscar_todos()
    
    # Preparar dados para o gráfico
    titulos = [jogo.titulo for jogo in jogos]
    precos = [jogo.preco for jogo in jogos]
    desenvolvedores = [jogo.desenvolvedor for jogo in jogos]

    return render_template(
        "graficos.html",
        titulos=titulos,
        precos=precos,
        desenvolvedores=desenvolvedores
    )

if __name__ == "__main__":
    app.run(debug=True)
