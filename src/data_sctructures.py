class Tupla:
    def __init__(self, chave, dados):
        self.chave = chave
        self.dados = dados

class Pagina:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.tuplas = []

    def adicionar_tupla(self, tupla):
        if len(self.tuplas) < self.tamanho_max:
            self.tuplas.append(tupla)
            return True
        else:
            return False

class Bucket:
    def __init__(self):
        self.entradas = []

    def adicionar_entrada(self, chave, pagina_ref):
        self.entradas.append((chave, pagina_ref))

class Tabela:
    def __init__(self, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.paginas = []
        self.buckets = []
        self.num_buckets = 0

    def adicionar_tupla(self, tupla):
        if self.paginas and self.paginas[-1].adicionar_tupla(tupla):
            return
        else:
            nova_pagina = Pagina(self.tamanho_pagina)
            nova_pagina.adicionar_tupla(tupla)
            self.paginas.append(nova_pagina)

    def inicializar_buckets(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [Bucket() for _ in range(num_buckets)]

    def funcao_hash(self, chave):
        return hash(chave) % self.num_buckets

    def construir_indice(self):
        self.inicializar_buckets(len(self.paginas))  # Um bucket por página, como exemplo
        for i, pagina in enumerate(self.paginas):
            for tupla in pagina.tuplas:
                indice_bucket = self.funcao_hash(tupla.chave)
                self.buckets[indice_bucket].adicionar_entrada(tupla.chave, i)

    def buscar(self, chave):
        indice_bucket = self.funcao_hash(chave)
        bucket = self.buckets[indice_bucket]
        paginas_acessadas = 0
        for entrada in bucket.entradas:
            paginas_acessadas += 1
            if entrada[0] == chave:
                return {'palavra': chave, 'página': entrada[1], 'páginas_acessadas': paginas_acessadas}
        return None
    
    def table_scan(self, limite):
        resultados = []
        contagem = 0
        for pagina in self.paginas:
            for tupla in pagina.tuplas:
                resultados.append(tupla)
                contagem += 1
                if contagem >= limite:
                    return resultados
        return resultados

    def calcular_estatisticas(self):
        total_entradas = 0
        colisoes = 0
        for bucket in self.buckets:
            if len(bucket.entradas) > 1:  # Mais de uma entrada indica uma colisão
                colisoes += len(bucket.entradas) - 1
            total_entradas += len(bucket.entradas)
        taxa_colisoes = colisoes / total_entradas if total_entradas > 0 else 0
        return {'taxa_colisoes': taxa_colisoes, 'total_colisoes': colisoes, 'total_entradas': total_entradas}