from flask import Flask, render_template, request, redirect, flash
import os
import re

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash_messages'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos


class MotorBuscaJogos:
    def __init__(self):
        self.jogos = []

    def carregar_jogos_de_arquivo(self, arquivo_caminho):
        try:
            with open(arquivo_caminho, 'r', encoding='utf-8') as file:
                self.jogos = []
                for linha in file:
                    dados = linha.strip().split(",")
                    jogo_id = int(dados[0])
                    titulo = dados[1]
                    desenvolvedor = dados[2]
                    preco = float(dados[3].replace(",", "."))
                    generos = dados[4:]
                    jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
                    self.jogos.append(jogo)
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")

    def buscar_todos(self):
        return self.jogos

    def buscar_por_preco(self, preco):
        return [jogo for jogo in self.jogos if jogo.preco == preco]

    def buscar_por_faixa_preco(self, preco_min, preco_max):
        return [jogo for jogo in self.jogos if preco_min <= jogo.preco <= preco_max]

    def buscar_por_genero(self, genero):
        return [jogo for jogo in self.jogos if genero in jogo.generos]

    def buscar_gratis(self):
        return [jogo for jogo in self.jogos if jogo.preco == 0]

    def obter_generos_unicos(self):
        generos = set()
        for jogo in self.jogos:
            generos.update(jogo.generos)
        return sorted(generos)


# Instância global do motor de busca
motor_busca = MotorBuscaJogos()


@app.route("/", methods=["GET", "POST"])
def index():
    filtros_visiveis = False
    jogos = []
    generos_disponiveis = []

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

    if request.method == "POST" and 'filtrar' in request.form:
        genero = request.form.get("genero")
        preco_min = request.form.get("preco_min")
        preco_max = request.form.get("preco_max")
        preco_exato = request.form.get("preco_exato")
        apenas_gratis = request.form.get("gratis") == "on"
        filtros_visiveis = True
        generos_disponiveis = motor_busca.obter_generos_unicos()

        # Aplicar filtros
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

        # Exibir mensagem se nenhum resultado for encontrado
        if not jogos:
            flash("Nenhum resultado encontrado com os filtros aplicados!", "warning")

    return render_template("index.html", filtros_visiveis=filtros_visiveis, jogos=jogos, generos=generos_disponiveis)


if __name__ == "__main__":
    app.run(debug=True)
