import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from src.data_sctructures import Tabela, Tupla

# Inicialização da tabela com um tamanho de página exemplo
tamanho_pagina = 100  # Defina conforme a necessidade ou faça ajustável pelo usuário
tabela = Tabela(tamanho_pagina)

def setup_gui(root):
    root.title("Índice Hash Estático")
    root.geometry("800x600")  # Define o tamanho da janela

    # Carregamento de Dados
    load_frame = tk.Frame(root)
    load_frame.pack(pady=10)
    load_button = tk.Button(load_frame, text="Carregar Dados", command=lambda: load_data())
    load_button.pack(side=tk.LEFT)
    load_status = tk.Label(load_frame, text="Nenhum arquivo carregado.")
    load_status.pack(side=tk.LEFT, padx=10)

    # Construção do Índice
    build_index_button = tk.Button(root, text="Construir Índice", command=lambda: build_index())
    build_index_button.pack(pady=10)

    # Busca
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT)
    search_button = tk.Button(search_frame, text="Buscar", command=lambda: search(search_entry.get()))
    search_button.pack(side=tk.LEFT, padx=10)
    search_result = tk.Label(root, text="")
    search_result.pack(pady=10)

    # Table Scan
    table_scan_frame = tk.Frame(root)
    table_scan_frame.pack(pady=10)
    table_scan_entry = tk.Entry(table_scan_frame)
    table_scan_entry.pack(side=tk.LEFT)
    table_scan_button = tk.Button(table_scan_frame, text="Table Scan", command=lambda: table_scan(table_scan_entry.get()))
    table_scan_button.pack(side=tk.LEFT, padx=10)
    table_scan_text = scrolledtext.ScrolledText(root, height=5)
    table_scan_text.pack(pady=10)

    # Estatísticas
    stats_text = scrolledtext.ScrolledText(root, height=5)
    stats_text.pack(pady=10)

def load_data():
    filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filename:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    palavra = line.strip()
                    tabela.adicionar_tupla(Tupla(palavra, None))  # Supondo que a palavra seja a chave e não haja dados adicionais
            load_status.config(text=f"Arquivo Carregado: {filename.split('/')[-1]}")
            messagebox.showinfo("Carregamento Concluído", "Dados carregados com sucesso na tabela.")
        except Exception as e:
            messagebox.showerror("Erro ao Carregar", f"Ocorreu um erro ao carregar o arquivo: {e}")

def build_index():
    # Lógica para construir o índice será implementada aqui
    pass

def search(query):
    # Lógica para buscar a chave será implementada aqui
    search_result.config(text=f"Resultado para '{query}': ...")

def table_scan(limit):
    # Lógica para realizar o table scan será implementada aqui
    table_scan_text.insert(tk.INSERT, f"Exibindo {limit} registros...\n")
