#Valadez Gutierrez David
import random
import tkinter as tk

# Función que genera números aleatorios
def numerosAleatorios(n):
    listaNumeros = [random.randint(0, 100) for _ in range(n)]
    return listaNumeros

#2. Paradigma divide y venceras
def dividir(listaNumeros, texto_subproblemas, texto_resultado):
    if len(listaNumeros) == 1:
        print("\nSuma: " + str(listaNumeros[0]))
        return listaNumeros[0]
    else:
        # Divide la lista
        mitad = len(listaNumeros) // 2

        # Muestra subproblemas
        print("\nMitad 1: " + str(listaNumeros[:mitad]) + " Mitad 2: " + str(listaNumeros[mitad:]))
        texto_subproblemas.insert(tk.END, "Mitad 1: " + str(listaNumeros[:mitad]) + " Mitad 2: " + str(listaNumeros[mitad:]) + "\n")

        #4. Recursividad
        suma_izquierda = dividir(listaNumeros[:mitad], texto_subproblemas, texto_resultado)
        suma_derecha = dividir(listaNumeros[mitad:], texto_subproblemas, texto_resultado)
        
        #3. Muestra la suma de los subproblemas
        print("\nSuma: " + str(suma_izquierda) + " + " + str(suma_derecha))
        texto_subproblemas.insert(tk.END, "Suma: " + str(suma_izquierda) + " + " + str(suma_derecha) + "\n")
        
        # Retorna la suma de las mitades
        return suma_izquierda + suma_derecha

def accionar():
    try:
        cantidad_numeros = int(cuadro_texto.get())
        lista_numeros_aleatorios = numerosAleatorios(cantidad_numeros)
        
        textoDirectorioR.delete("1.0", tk.END)
        textoDirectorioR.insert(tk.END, '\n'.join(map(str, lista_numeros_aleatorios)))

        texto_subproblemas.delete("1.0", tk.END)
        texto_resultado.delete("1.0", tk.END)
        
        suma = dividir(lista_numeros_aleatorios, texto_subproblemas, texto_resultado)
        texto_resultado.insert(tk.END, "Resultado de la suma: " + str(suma))
    except ValueError:
        print("Error: Debe ingresar un número válido para la cantidad de números aleatorios.")

#1. GUI TKINTER
root = tk.Tk()
root.configure(bg='black')
root.geometry("440x560")
root.title("SUMA DE NUMEROS")

cuadro_texto = tk.Entry(root, width=40)
cuadro_texto.pack(pady=10)

textoDirectorioR = tk.Text(root, wrap=tk.WORD, width=40, height=5, bg='white')
textoDirectorioR.pack(padx=5)

texto_subproblemas = tk.Text(root, wrap=tk.WORD, width=40, height=20, bg='white')
texto_subproblemas.pack(padx=5, pady=10)

texto_resultado = tk.Text(root, wrap=tk.WORD, width=40, height=1, bg='white')
texto_resultado.pack(padx=5, pady=10)

botonDirectorioRemitente = tk.Button(root, text="Accionar", command=accionar)
botonDirectorioRemitente.pack(pady=10)

botonCerrar = tk.Button(root, text="Cerrar", command=root.quit)
botonCerrar.pack(pady=10)

root.mainloop()
