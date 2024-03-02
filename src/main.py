import tkinter as tk
from gui import setup_gui

def main():
    """
    Função principal que inicializa a janela principal do Tkinter e configura a interface gráfica do usuário (GUI).
    """
    # Cria a janela principal
    root = tk.Tk()

    # Configura a GUI dentro da janela principal
    setup_gui(root)

    # Inicia o loop principal da interface gráfica
    # Isso mantém a janela aberta e responsiva aos eventos do usuário
    root.mainloop()

if __name__ == "__main__":
    # Garante que este script só execute a função main quando executado diretamente,
    # e não quando importado como um módulo.
    main()