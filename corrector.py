import language_tool_python

# Corrector en español
tool = language_tool_python.LanguageTool('es')

print("=== Corrector de Ortografía ===")
texto = input("Escribe el texto que quieres corregir:\n")

# Buscar errores
errores = tool.check(texto)

# Corregir texto
texto_corregido = language_tool_python.utils.correct(texto, errores)

print("\nTexto original:")
print(texto)

print("\nTexto corregido:")
print(texto_corregido)

print("\nErrores encontrados:")
for error in errores:
    print(f"- {error.message}")
    print(f"  Sugerencias: {error.replacements}")