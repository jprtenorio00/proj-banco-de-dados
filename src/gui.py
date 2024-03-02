import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from data_sctructures import Tabela, Tupla

# Inicialização da tabela com um tamanho de página exemplo
tamanho_pagina = 100  # Este valor pode ser ajustado conforme necessário
tabela = Tabela(tamanho_pagina)

# Declarando variáveis globais para acessá-las em diferentes funções
load_status = None
search_result = None
table_scan_text = None
stats_text = None

def setup_gui(root):
    global load_status, search_result, table_scan_text, stats_text

    root.title("Índice Hash Estático")
    root.geometry("1024x768")  # Ajuste o tamanho da janela conforme necessário

    # Carregamento de Dados
    load_frame = tk.Frame(root)
    load_frame.pack(pady=10)
    load_button = tk.Button(load_frame, text="Carregar Dados", command=load_data)
    load_button.pack(side=tk.LEFT)
    load_status = tk.Label(load_frame, text="Nenhum arquivo carregado.")
    load_status.pack(side=tk.LEFT, padx=10)

    # Construção do Índice
    build_index_button = tk.Button(root, text="Construir Índice", command=build_index)
    build_index_button.pack(pady=10)

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
    global load_status

    filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filename:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    palavra = line.strip()
                    tabela.adicionar_tupla(Tupla(palavra, palavra))  # Use a palavra como dados também, para simplificar
            load_status.config(text=f"Arquivo Carregado: {filename.split('/')[-1]}")
            messagebox.showinfo("Carregamento Concluído", "Dados carregados com sucesso na tabela.")
        except Exception as e:
            messagebox.showerror("Erro ao Carregar", f"Ocorreu um erro ao carregar o arquivo: {e}")

def build_index():
    try:
        tabela.construir_indice()  # Supõe-se que existe um método construir_indice na classe Tabela
        messagebox.showinfo("Construir Índice", "Índice construído com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro ao Construir Índice", f"Ocorreu um erro ao construir o índice: {e}")

def search(query):
    resultado = tabela.buscar(query)  # Supõe-se que existe um método buscar na classe Tabela
    if resultado:
        search_result.config(text="Chave encontrada.")
    else:
        search_result.config(text="Chave não encontrada.")

def table_scan(limit):
    global table_scan_text
    try:
        limit = int(limit)
        resultados = tabela.table_scan(limit)
        table_scan_text.delete('1.0', tk.END)  # Limpa o texto antes de inserir novos resultados
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
    stats_text.delete('1.0', tk.END)  # Limpa o texto antes de inserir novas estatísticas
    stats_text.insert(tk.END, f"Total de Entradas: {estatisticas['total_entradas']}\n")
    stats_text.insert(tk.END, f"Total de Colisões: {estatisticas['total_colisoes']}\n")
    stats_text.insert(tk.END, f"Taxa de Colisões: {estatisticas['taxa_colisoes']:.2f}\n")