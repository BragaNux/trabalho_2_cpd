class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos 

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        def inserir_no(no_atual, novo_no):
            if novo_no.jogo.preco < no_atual.jogo.preco:
                if no_atual.esquerda is None:
                    no_atual.esquerda = novo_no
                else:
                    inserir_no(no_atual.esquerda, novo_no)
            else:
                if no_atual.direita is None:
                    no_atual.direita = novo_no
                else:
                    inserir_no(no_atual.direita, novo_no)

        novo_no = NoJogo(jogo)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            inserir_no(self.raiz, novo_no)

    def buscar_por_preco(self, preco):
        resultados = []

        def buscar(no_atual):
            if no_atual is None:
                return
            if no_atual.jogo.preco == preco:
                resultados.append(no_atual.jogo)
            if preco < no_atual.jogo.preco:
                buscar(no_atual.esquerda)
            else:
                buscar(no_atual.direita)

        buscar(self.raiz)
        return resultados

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        resultados = []

        def buscar(no_atual):
            if no_atual is None:
                return
            if preco_minimo <= no_atual.jogo.preco <= preco_maximo:
                resultados.append(no_atual.jogo)
            if preco_minimo < no_atual.jogo.preco:
                buscar(no_atual.esquerda)
            if preco_maximo > no_atual.jogo.preco:
                buscar(no_atual.direita)

        buscar(self.raiz)
        return resultados

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []
            self.genero_para_jogos[genero].append(jogo)

    def obter_jogos(self, genero):
        return self.genero_para_jogos.get(genero, [])

class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def carregar_jogos_de_arquivo(self, arquivo):
        with open(arquivo, "r") as file:
            for linha in file:
                dados = linha.strip().split(",")
                jogo_id = int(dados[0])
                titulo = dados[1]
                desenvolvedor = dados[2]
                preco = int(dados[3])
                generos = dados[4:]
                jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
                self.catalogo_jogos.inserir(jogo)
                self.generos.adicionar_jogo(jogo)

    def buscar_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def buscar_por_faixa_preco(self, preco_min, preco_max):
        return self.catalogo_jogos.busca_por_faixa_preco(preco_min, preco_max)

    def buscar_por_genero(self, genero):
        return self.generos.obter_jogos(genero)

#testes
if __name__ == "__main__":
    motor_busca = MotorBuscaJogos()
    motor_busca.carregar_jogos_de_arquivo("jogos.txt")

    print("Busca por preço exato (150):")
    for jogo in motor_busca.buscar_por_preco(150):
        print(f"{jogo.titulo} - R${jogo.preco}")

    print("\nBusca por faixa de preços (50 a 200):")
    for jogo in motor_busca.buscar_por_faixa_preco(50, 200):
        print(f"{jogo.titulo} - R${jogo.preco}")

    print("\nBusca por gênero (RPG):")
    for jogo in motor_busca.buscar_por_genero("RPG"):
        print(f"{jogo.titulo} - Gêneros: {', '.join(jogo.generos)}")
