class Tupla:
    def __init__(self, chave, dados):
        self.chave = chave  # A chave única para a tupla, por exemplo, a palavra
        self.dados = dados  # Os dados associados à chave, se houver

class Pagina:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max  # O tamanho máximo da página (número de tuplas que pode conter)
        self.tuplas = []  # Lista para armazenar as tuplas

    def adicionar_tupla(self, tupla):
        if len(self.tuplas) < self.tamanho_max:
            self.tuplas.append(tupla)
            return True
        else:
            return False  # A página está cheia

class Bucket:
    def __init__(self):
        self.entradas = []  # Lista para armazenar entradas (chave, referência à página)

    def adicionar_entrada(self, chave, pagina_ref):
        self.entradas.append((chave, pagina_ref))

class Tabela:
    def __init__(self, tamanho_pagina):
        self.tamanho_pagina = tamanho_pagina
        self.paginas = []
        self.buckets = []  # Inicialmente vazio, será preenchido após a definição do número de buckets

    def adicionar_tupla(self, tupla):
        # Tenta adicionar a tupla na última página, se houver espaço
        if self.paginas and self.paginas[-1].adicionar_tupla(tupla):
            return
        else:
            # Cria uma nova página e adiciona a tupla
            nova_pagina = Pagina(self.tamanho_pagina)
            nova_pagina.adicionar_tupla(tupla)
            self.paginas.append(nova_pagina)

    def inicializar_buckets(self, num_buckets):
        self.buckets = [Bucket() for _ in range(num_buckets)]