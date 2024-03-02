import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from data_sctructures import Tabela, Tupla

tamanho_pagina = 100
tabela = Tabela(tamanho_pagina)
load_status = None
search_result = None
table_scan_text = None
stats_text = None

def setup_gui(root):
    global load_status, search_result, table_scan_text, stats_text, tamanho_pagina_var
    tamanho_pagina_var = tk.IntVar(value=100)

    root.title("Índice Hash Estático")
    root.geometry("1024x768")

    # Carregamento de Dados
    load_frame = tk.Frame(root)
    load_frame.pack(pady=10)
    load_button = tk.Button(load_frame, text="Carregar Dados", command=load_data)
    load_button.pack(side=tk.LEFT)
    load_status = tk.Label(load_frame, text="Nenhum arquivo carregado.")
    load_status.pack(side=tk.LEFT, padx=10)

    # Tamanho da Página
    tamanho_pagina_frame = tk.Frame(root)
    tamanho_pagina_frame.pack(pady=10)
    tk.Label(tamanho_pagina_frame, text="Tamanho da Página:").pack(side=tk.LEFT)
    tamanho_pagina_entry = tk.Entry(tamanho_pagina_frame, textvariable=tamanho_pagina_var)
    tamanho_pagina_entry.pack(side=tk.LEFT)

    def set_tamanho_pagina():
        try:
            valor = int(tamanho_pagina_entry.get())
            tamanho_pagina_var.set(valor)
            messagebox.showinfo("Tamanho da Página", f"Tamanho da página definido como {valor}.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

    tamanho_pagina_button = tk.Button(tamanho_pagina_frame, text="Definir Tamanho", command=set_tamanho_pagina)
    tamanho_pagina_button.pack(side=tk.LEFT, padx=10)

    # Busca
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)
    search_entry = tk.Entry(search_frame, width=50)
    search_entry.pack(side=tk.LEFT)
    search_button = tk.Button(search_frame, text="Buscar", command=lambda: search(search_entry.get()))
    search_button.pack(side=tk.LEFT, padx=10)
    search_result = tk.Label(root, text="")
    search_result.pack(pady=10)

    # Table Scan
    table_scan_frame = tk.Frame(root)
    table_scan_frame.pack(pady=10)
    table_scan_entry = tk.Entry(table_scan_frame, width=20)
    table_scan_entry.pack(side=tk.LEFT)
    table_scan_button = tk.Button(table_scan_frame, text="Table Scan", command=lambda: table_scan(table_scan_entry.get()))
    table_scan_button.pack(side=tk.LEFT, padx=10)
    table_scan_text = scrolledtext.ScrolledText(root, height=10, width=100)
    table_scan_text.pack(pady=10)

    # Estatísticas
    stats_label = tk.Label(root, text="Estatísticas:")
    stats_label.pack(pady=10)
    stats_text = scrolledtext.ScrolledText(root, height=5, width=100)
    stats_text.pack(pady=10)

    # Botão para Mostrar Estatísticas
    stats_button = tk.Button(root, text="Mostrar Estatísticas", command=mostrar_estatisticas)
    stats_button.pack(pady=10)

def load_data():
    global load_status, tabela

    filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filename:
        try:
            tabela = Tabela(tamanho_pagina_var.get())
            with open(filename, 'r') as file:
                for line in file:
                    palavra = line.strip()
                    tabela.adicionar_tupla(Tupla(palavra, palavra))
            load_status.config(text=f"Arquivo Carregado: {filename.split('/')[-1]}")
            tabela.construir_indice()
            messagebox.showinfo("Carregamento e Construção de Índice", "Dados carregados e índice construído com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro ao Carregar", f"Ocorreu um erro ao carregar o arquivo: {e}")

def build_index():
    try:
        tabela.construir_indice()
        messagebox.showinfo("Construir Índice", "Índice construído com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro ao Construir Índice", f"Ocorreu um erro ao construir o índice: {e}")

def search(query):
    resultado = tabela.buscar(query)
    if resultado:
        search_result.config(text=f"Palavra: '{resultado['palavra']}', Página: {resultado['página']}, Páginas Acessadas: {resultado['páginas_acessadas']}")
    else:
        search_result.config(text="Palavra não encontrada.")

def table_scan(limit):
    global table_scan_text
    try:
        limit = int(limit)
        resultados = tabela.table_scan(limit)
        table_scan_text.delete('1.0', tk.END)
        for tupla in resultados:
            #table_scan_text.insert(tk.END, f"{tupla.chave}: {tupla.dados}\n")
            table_scan_text.insert(tk.END, f"{tupla.chave}\n")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o limite de registros.")
    except Exception as e:
        messagebox.showerror("Erro ao Realizar Table Scan", f"Ocorreu um erro: {e}")

def mostrar_estatisticas():
    global stats_text
    estatisticas = tabela.calcular_estatisticas()
    stats_text.delete('1.0', tk.END)
    stats_text.insert(tk.END, f"Total de Entradas: {estatisticas['total_entradas']}\n")
    stats_text.insert(tk.END, f"Total de Colisões: {estatisticas['total_colisoes']}\n")
    stats_text.insert(tk.END, f"Taxa de Colisões: {estatisticas['taxa_colisoes']:.2f}\n")