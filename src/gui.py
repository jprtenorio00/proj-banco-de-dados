import tkinter as tk

def setup_gui(root):
    root.title("Índice Hash Estático")
    root.geometry("800x600")

    # Aqui você pode adicionar widgets à janela principal
    label = tk.Label(root, text="Bem-vindo ao Sistema de Índice Hash Estático!")
    label.pack(pady=20)
