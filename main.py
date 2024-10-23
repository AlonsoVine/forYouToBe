import tkinter as tk
from tkinter import filedialog, messagebox
from utils.download_manager import descargar_audio


# Función para seleccionar la carpeta de descarga
def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        carpeta_label.config(text=carpeta)
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")


# Función para descargar las canciones seleccionadas
def iniciar_descarga():
    formato = formato_var.get()
    url_list = urls_text.get("1.0", tk.END).strip().splitlines()
    carpeta = carpeta_label.cget("text")

    if not url_list:
        messagebox.showerror("Error", "La lista de URLs está vacía.")
    elif not carpeta:
        messagebox.showerror("Error", "No has seleccionado una carpeta de destino.")
    else:
        for url in url_list:
            descargar_audio(url, carpeta, formato)
        messagebox.showinfo("Éxito", f"Descarga completada en formato {formato}.")


# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de Música")

# Selector de formato
formato_var = tk.StringVar(value="mp3")
formato_label = tk.Label(root, text="Formato de descarga:")
formato_label.pack()
formato_selector = tk.OptionMenu(root, formato_var, "mp3", "wav", "flac")
formato_selector.pack()

# Campo para ingresar las URLs
urls_label = tk.Label(root, text="Lista de URLs de YouTube:")
urls_label.pack()
urls_text = tk.Text(root, height=10)
urls_text.pack()

# Botón para seleccionar la carpeta de destino
carpeta_button = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta)
carpeta_button.pack()
carpeta_label = tk.Label(root, text="")
carpeta_label.pack()

# Botón para iniciar la descarga
descargar_button = tk.Button(root, text="Descargar Todas", command=iniciar_descarga)
descargar_button.pack()

# Ejecutar la ventana
root.mainloop()
