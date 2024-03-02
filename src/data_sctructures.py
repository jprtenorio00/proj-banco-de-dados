class Tupla:
    """Representa uma tupla, contendo a chave de busca e os dados associados."""
    def __init__(self, chave, dados):
        self.chave = chave
        self.dados = dados

class Pagina:
    """Representa uma página, que armazena um conjunto limitado de tuplas."""
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.tuplas = []

    def adicionar_tupla(self, tupla):
        """Adiciona uma tupla à página se houver espaço disponível."""
        if len(self.tuplas) < self.tamanho_max:
            self.tuplas.append(tupla)
            return True
        return False

class Bucket:
    """Representa um bucket no índice hash, que pode armazenar múltiplas tuplas."""
    def __init__(self):
        self.entradas = []

    def adicionar_entrada(self, tupla):
        """Adiciona uma tupla ao bucket."""
        self.entradas.append(tupla)

class Tabela:
    """Representa a tabela completa, contendo páginas de tuplas e buckets para o índice hash."""
    def __init__(self, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.paginas = []
        self.buckets = []
        self.num_buckets = 0

    def adicionar_tupla(self, tupla):
        """Adiciona uma tupla à tabela, em uma nova página se necessário."""
        if not self.paginas or not self.paginas[-1].adicionar_tupla(tupla):
            nova_pagina = Pagina(self.tamanho_pagina)
            nova_pagina.adicionar_tupla(tupla)
            self.paginas.append(nova_pagina)

    def inicializar_buckets(self, num_buckets):
        """Inicializa os buckets com base em um número especificado."""
        self.num_buckets = num_buckets
        self.buckets = [Bucket() for _ in range(num_buckets)]

    def funcao_hash(self, chave):
        """Calcula o índice do bucket para uma dada chave usando uma função hash simples."""
        return hash(chave) % self.num_buckets

    def construir_indice(self):
        """Constrói o índice hash mapeando cada tupla para um bucket com base na chave."""
        self.inicializar_buckets(self.calcular_num_buckets())
        for pagina in self.paginas:
            for tupla in pagina.tuplas:
                indice_bucket = self.funcao_hash(tupla.chave)
                self.buckets[indice_bucket].adicionar_entrada(tupla)

    def buscar(self, chave):
        """Busca tuplas correspondentes à chave fornecida e retorna suas referências de página."""
        indice_bucket = self.funcao_hash(chave)
        bucket = self.buckets[indice_bucket]
        return [(tupla, self.encontrar_pagina_ref(tupla)) for tupla in bucket.entradas if tupla.chave == chave]

    def table_scan(self, limite):
        """Realiza um table scan limitado, retornando as primeiras 'limite' tuplas."""
        return [tupla for pagina in self.paginas for tupla in pagina.tuplas][:limite]

    def calcular_estatisticas(self):
        """Calcula estatísticas sobre o índice, como total de entradas e taxa de colisões."""
        total_entradas = sum(len(bucket.entradas) for bucket in self.buckets)
        colisoes = sum(len(bucket.entradas) - 1 for bucket in self.buckets if len(bucket.entradas) > 1)
        taxa_colisoes = colisoes / total_entradas if total_entradas > 0 else 0
        return {'total_entradas': total_entradas, 'total_colisoes': colisoes, 'taxa_colisoes': taxa_colisoes}

    def calcular_num_buckets(self):
        """Calcula o número ideal de buckets com base no número total de tuplas e um fator de carga."""
        NR = sum(len(pagina.tuplas) for pagina in self.paginas)
        FR = 10  # Fator de carga desejado (número de tuplas por bucket)
        return max(NR // FR, 1)

    def encontrar_pagina_ref(self, tupla):
        """Encontra a referência da página para uma dada tupla."""
        for i, pagina in enumerate(self.paginas):
            if tupla in pagina.tuplas:
                return i
        return None