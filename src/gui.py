import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from data_sctructures import Tabela, Tupla

class HashIndexGUI:
    def __init__(self, root):
        self.root = root
        self.tabela = Tabela(tamanho_pagina=100)
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Índice Hash Estático")
        self.root.geometry("1024x768")

        self.setup_load_frame()
        self.setup_page_size_frame()
        self.setup_search_frame()
        self.setup_table_scan_frame()
        self.setup_stats_display()

    def setup_load_frame(self):
        load_frame = tk.Frame(self.root)
        load_frame.pack(pady=10)

        load_button = tk.Button(load_frame, text="Carregar Dados", command=self.load_data)
        load_button.pack(side=tk.LEFT)

        self.load_status = tk.Label(load_frame, text="Nenhum arquivo carregado.")
        self.load_status.pack(side=tk.LEFT, padx=10)

    def setup_page_size_frame(self):
        page_size_frame = tk.Frame(self.root)
        page_size_frame.pack(pady=10)

        self.page_size_var = tk.IntVar(value=100)
        tk.Label(page_size_frame, text="Tamanho da Página:").pack(side=tk.LEFT)
        page_size_entry = tk.Entry(page_size_frame, textvariable=self.page_size_var)
        page_size_entry.pack(side=tk.LEFT)

        set_page_size_button = tk.Button(page_size_frame, text="Definir Tamanho", command=self.set_page_size)
        set_page_size_button.pack(side=tk.LEFT, padx=10)

    def setup_search_frame(self):
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(search_frame, width=50)
        self.search_entry.pack(side=tk.LEFT)

        search_button = tk.Button(search_frame, text="Buscar", command=self.search)
        search_button.pack(side=tk.LEFT, padx=10)

        self.search_result = tk.Label(self.root, text="")
        self.search_result.pack(pady=10)

    def setup_table_scan_frame(self):
        table_scan_frame = tk.Frame(self.root)
        table_scan_frame.pack(pady=10)

        self.table_scan_entry = tk.Entry(table_scan_frame, width=20)
        self.table_scan_entry.pack(side=tk.LEFT)

        table_scan_button = tk.Button(table_scan_frame, text="Table Scan", command=self.table_scan)
        table_scan_button.pack(side=tk.LEFT, padx=10)

        self.table_scan_text = scrolledtext.ScrolledText(self.root, height=10, width=100)
        self.table_scan_text.pack(pady=10)

    def setup_stats_display(self):
        stats_label = tk.Label(self.root, text="Estatísticas:")
        stats_label.pack(pady=10)

        self.stats_text = scrolledtext.ScrolledText(self.root, height=5, width=100)
        self.stats_text.pack(pady=10)

        stats_button = tk.Button(self.root, text="Mostrar Estatísticas", command=self.show_statistics)
        stats_button.pack(pady=10)

    def load_data(self):
        filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            try:
                self.tabela = Tabela(self.page_size_var.get())
                with open(filename, 'r') as file:
                    for line in file:
                        palavra = line.strip()
                        self.tabela.adicionar_tupla(Tupla(palavra, palavra))
                self.load_status.config(text=f"Arquivo Carregado: {filename.split('/')[-1]}")
                self.tabela.construir_indice()
                messagebox.showinfo("Carregamento e Construção de Índice", "Dados carregados e índice construído com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro ao Carregar", f"Ocorreu um erro ao carregar o arquivo: {e}")

    def set_page_size(self):
        try:
            valor = self.page_size_var.get()
            messagebox.showinfo("Tamanho da Página", f"Tamanho da página definido como {valor}.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

    def search(self):
        query = self.search_entry.get()
        resultados = self.tabela.buscar(query)
        
        if resultados:
            resultado_texto = f"{len(resultados)} resultado(s) encontrado(s) para '{query}':\n\n"
            paginas_acessadas = 0
            for tupla, pagina_ref in resultados:
                paginas_acessadas += 1
                resultado_texto += f"Chave: '{tupla.chave}', Página: {pagina_ref}, Páginas Acessadas: {paginas_acessadas}\n"
            self.search_result.config(text=resultado_texto)
        else:
            self.search_result.config(text="Nenhum resultado encontrado.")

    def table_scan(self):
        try:
            limit = int(self.table_scan_entry.get())
            resultados = self.tabela.table_scan(limit)
            
            self.table_scan_text.delete('1.0', tk.END)
            for tupla in resultados:
                self.table_scan_text.insert(tk.END, f"Chave: '{tupla.chave}'\n")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido para o limite.")

    def show_statistics(self):
        estatisticas = self.tabela.calcular_estatisticas()
        
        self.stats_text.delete('1.0', tk.END)
        self.stats_text.insert(tk.END, f"Total de Entradas: {estatisticas['total_entradas']}\n")
        self.stats_text.insert(tk.END, f"Total de Colisões: {estatisticas['total_colisoes']}\n")
        self.stats_text.insert(tk.END, f"Taxa de Colisões: {estatisticas['taxa_colisoes'] * 100:.2f}%\n")

def setup_gui(root):
    HashIndexGUI(root)

if __name__ == "__main__":
    root = tk.Tk()
    setup_gui(root)
    root.mainloop()