#Valadez Gutierrez David
import random
import tkinter as tk

#Funcion que genera numeros aleatorios
def numerosAleatorios(n):
    listaNumeros = [0] * n #Asigna el espacio de la lista multiplicado por n que seran los numeros ingresados

    for i in range(n): #Itera en la cantidad de numeros ingresados
        listaNumeros[i] = random.randint(0, 100) #Genera los numero aleatorios y los ingresa a la lista

    return listaNumeros

#2. Paradigma divide y venceras
def dividir(listaNumeros, texto_subproblemas, texto_resultado):
    if len(listaNumeros) == 1: #Identificar si alguna mita es de un solo numero 
        print("\nSuma: " + str(listaNumeros[0]))
        return listaNumeros[0]
    else:
        #Divide la lista
        mitad = len(listaNumeros) // 2

        #Muestra subproblemas
        print("\nMitad 1: " + str(listaNumeros[:mitad]) + " Mitad 2: " + str(listaNumeros[mitad:]))
        texto_subproblemas.insert(tk.END, "Mitad 1: " + str(listaNumeros[:mitad]) + " Mitad 2: " + str(listaNumeros[mitad:]) + "\n")

        #4. Recursividad
        suma_izquierda = dividir(listaNumeros[:mitad], texto_subproblemas, texto_resultado)
        suma_derecha = dividir(listaNumeros[mitad:], texto_subproblemas, texto_resultado)
        
        #3. Muestra la suma de los subproblemas
        print("\nSuma: " + str(suma_izquierda) + " + " + str(suma_derecha))
        texto_subproblemas.insert(tk.END, "Suma: " + str(suma_izquierda) + " + " + str(suma_derecha) + "\n")
        
        #Retorna la suma de las mitades
        return suma_izquierda + suma_derecha

def accionar():
    contenido_texto = textoDirectorioR.get("1.0", tk.END)
    listaNumeros = [int(num) for num in contenido_texto.split() if num.isdigit()]
    
    texto_subproblemas.delete("1.0", tk.END)
    texto_resultado.delete("1.0", tk.END)
    
    suma = dividir(listaNumeros, texto_subproblemas, texto_resultado)
    texto_resultado.insert(tk.END, "Resultado de la suma: " + str(suma))

#Implementacion de la funcion
listaNumerosAleatorios = numerosAleatorios(10)

print('\nLista de numeros', listaNumerosAleatorios)

#1. GUI TKINTER
root = tk.Tk()
root.configure(bg='black')
root.geometry("440x520")
root.title("SUMA DE NUMEROS")

textoDirectorioR = tk.Text(root, wrap=tk.WORD, width=40, height=5, bg='white')
textoDirectorioR.insert(tk.END, '\n'.join(map(str, listaNumerosAleatorios)))
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
