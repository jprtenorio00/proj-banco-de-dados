import tkinter as tk
from tkinter import filedialog, scrolledtext

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

    # Funções Dummy (serão implementadas posteriormente)
    def load_data():
        filename = filedialog.askopenfilename()
        if filename:
            load_status.config(text=f"Arquivo Carregado: {filename.split('/')[-1]}")
            # Aqui você adicionará a lógica para carregar e processar o arquivo

    def build_index():
        # Lógica para construir o índice
        pass

    def search(query):
        # Lógica para buscar a chave
        search_result.config(text=f"Resultado para '{query}': ...")

    def table_scan(limit):
        # Lógica para realizar o table scan
        table_scan_text.insert(tk.INSERT, f"Exibindo {limit} registros...\n")
