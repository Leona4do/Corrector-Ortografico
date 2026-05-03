import tkinter as tk
from tkinter import scrolledtext
import language_tool_python

tool = language_tool_python.LanguageTool('es')

def corregir_texto():
    texto = entrada.get("1.0", tk.END)
    errores = tool.check(texto)
    texto_corregido = language_tool_python.utils.correct(texto, errores)

    # Mostrar texto corregido
    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, texto_corregido)
    salida.config(state="disabled")

    # Limpiar resaltado anterior
    entrada.tag_remove("error", "1.0", tk.END)

    # Resaltar errores
    for error in errores:
        start = f"1.0+{error.offset}c"
        end = f"1.0+{error.offset + error.error_length}c"
        entrada.tag_add("error", start, end)

    entrada.tag_config("error", background="#ff4d4d")

    # Contador
    contador.config(text=f"Errores encontrados: {len(errores)}")

def limpiar():
    entrada.delete("1.0", tk.END)
    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.config(state="disabled")
    contador.config(text="Errores encontrados: 0")

# Ventana
ventana = tk.Tk()
ventana.title("Corrector Ortográfico PRO")
ventana.geometry("800x600")
ventana.configure(bg="#121212")

# Título
titulo = tk.Label(
    ventana,
    text="Corrector Ortográfico PRO",
    fg="white",
    bg="#121212",
    font=("Segoe UI", 18, "bold")
)
titulo.pack(pady=10)

# Entrada
lbl1 = tk.Label(ventana, text="Texto original", fg="white", bg="#121212")
lbl1.pack()

entrada = scrolledtext.ScrolledText(
    ventana,
    height=10,
    font=("Consolas", 11),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white"
)
entrada.pack(padx=10, pady=5, fill="both")

# Botones
frame_botones = tk.Frame(ventana, bg="#121212")
frame_botones.pack(pady=10)

btn_corregir = tk.Button(
    frame_botones,
    text="Corregir",
    command=corregir_texto,
    bg="#4CAF50",
    fg="white",
    width=15,
    font=("Segoe UI", 10, "bold")
)
btn_corregir.pack(side="left", padx=10)

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar,
    bg="#f44336",
    fg="white",
    width=15,
    font=("Segoe UI", 10, "bold")
)
btn_limpiar.pack(side="left", padx=10)

# Contador
contador = tk.Label(
    ventana,
    text="Errores encontrados: 0",
    fg="#00ffcc",
    bg="#121212",
    font=("Segoe UI", 10)
)
contador.pack()

# Salida
lbl2 = tk.Label(ventana, text="Texto corregido", fg="white", bg="#121212")
lbl2.pack()

salida = scrolledtext.ScrolledText(
    ventana,
    height=10,
    font=("Consolas", 11),
    bg="#1e1e1e",
    fg="#00ffcc"
)
salida.pack(padx=10, pady=5, fill="both")
salida.config(state="disabled")

ventana.mainloop()