from tkinter import tk

class Producto:
    def __init__(self,precio):
        self.precio = precio

    def buscarProducto(nombreProducto):
        tk.messagebox.showinfo(message="Buscando producto", tittle="Buscando")

    def verProducto(producto):
        tk.messagebox.showinfo(message="Mostrando producto", tittle="Mostrando")
