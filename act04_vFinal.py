#Equipo 11
#Back David Valadez Gutierrez
#Front Enrique Eduardo Lozano Aceves
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import time

class EditarCadenaApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='black')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)
        self.frame.configure(bg='black')

        self.button_frame = tk.Frame(self.frame, bg='black')
        self.button_frame.pack(side='right', padx=10, pady=10, fill='y')

        self.text_frame = tk.Frame(self.frame, bg='black')
        self.text_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)

        self.mostrar_widgets()

    def mostrar_widgets(self):
        # Botones
        self.button_cargar_csv = tk.Button(self.button_frame, text="CARGAR CSV", padx=10, pady=5, command=self.cargar_csv)
        self.button_cargar_csv.pack(side='top', pady=5, fill='x')

        self.button_obtener_info = tk.Button(self.button_frame, text="SELECCIONAR CELDA", padx=10, pady=5, command=self.obtener_informacion)
        self.button_obtener_info.pack(side='top', pady=5, fill='x')

        self.button_accionar = tk.Button(self.button_frame, text="ACCIONAR", padx=10, pady=5, command=self.realizar_modificaciones)
        self.button_accionar.pack(side='top', pady=5, fill='x')

        self.button_generar_csv = tk.Button(self.button_frame, text="GENERAR CSV", padx=10, pady=5, command=self.generar_csv)
        self.button_generar_csv.pack(side='top', pady=5, fill='x')

        self.button_mostrar_combinacion = tk.Button(self.button_frame, text="MOSTRAR COMBINACIÓN", padx=10, pady=5, command=self.show_substring)
        self.button_mostrar_combinacion.pack(side='top', pady=5, fill='x')

        # Campos de texto y labels
        self.text_widget = ScrolledText(self.text_frame, height=20, width=50)
        self.text_widget.pack(side='left', fill='both', expand=True)

        self.label_selected_cell = tk.Label(self.text_frame, height=2, width=50, text="INFO. CELDA SELECCIONADA", bg='black', fg='white')
        self.label_selected_cell.pack(side='top', fill='x')

        self.texto_celda = tk.Entry(self.text_frame)
        self.texto_celda.pack(side='top', fill='x')

        self.label_selected_file_name = tk.Label(self.text_frame, height=2, width=50, text="INGRESA NOMBRE DE ARCHIVO", bg='black', fg='white')
        self.label_selected_file_name.pack(side='top', fill='x')

        self.label_selected_name = tk.Text(self.text_frame, height=2, width=50)
        self.label_selected_name.pack(side='top', fill='x')

        self.label_selected_substr1 = tk.Label(self.text_frame, height=2, width=50, text="Subcadena a combinar 1:", bg='black', fg='white')
        self.label_selected_substr1.pack(side='top', fill='x')

        self.entry_selected_substr1 = tk.Entry(self.text_frame)
        self.entry_selected_substr1.pack(side='top', fill='x')

        self.label_selected_substr2 = tk.Label(self.text_frame, height=2, width=50, text="Subcadena a combinar 2:", bg='black', fg='white')
        self.label_selected_substr2.pack(side='top', fill='x')

        self.entry_selected_substr2 = tk.Entry(self.text_frame)
        self.entry_selected_substr2.pack(side='top', fill='x')

        # Etiqueta para mostrar el tiempo de ejecución
        self.label_execution_time = tk.Label(self.button_frame, text="Tiempo de ejecución: ", bg='black', fg='white')
        self.label_execution_time.pack(side='top', pady=5, fill='x')

    def cargar_csv(self):
        archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if archivo:
            self.data = pd.read_csv(archivo)

    def obtener_informacion(self):
        celda = self.texto_celda.get()
        try:
            fila, columna = map(int, celda.split(','))
            self.selected_cell_value = self.data.iloc[fila - 1, columna - 1]

            self.label_selected_cell.config(text=f"{self.selected_cell_value}")
            self.text_widget.insert(tk.END, f"{self.selected_cell_value}\n")

        except Exception as e:
            self.label_selected_cell.config(text=f"Error: {str(e)}")


    def realizar_modificaciones(self):
        # Guardar el tiempo de inicio
        start_time = time.time()

        # Definir listas de posiciones y caracteres
        posiciones = self.data['posicion'].tolist() 
        caracteres = self.data['alteracion'].tolist() 

        # Leer la cadena
        cadena = self.selected_cell_value

        # Cambiar la posición en la cadena
        cadena_modificada = cadena

        for i in range(len(posiciones)):
            time.sleep(.01) #Añade mas tiempo para comprobar de mejro manera el tiempo
            pos = posiciones[i]
            if 0 <= pos < len(cadena_modificada):
                cadena_modificada = cadena_modificada[:pos] + caracteres[i] + cadena_modificada[pos + 1:]

        # Crear una lista de todas las cadenas modificadas
        cadenas_modificadas = [cadena_modificada]

        # Recorrer la cadena de dos en dos posiciones y generar subcadenas de 5 caracteres
        subcadenas = [cadena[i:i+5] for i in range(0, len(cadena), 2) if i+5 <= len(cadena)]

        # Realizar modificaciones a la cadena principal
        for i in range(len(posiciones)):
            time.sleep(.01) #Añade mas tiempo para comprobar de mejro manera el tiempo
            pos = posiciones[i]
            if 0 <= pos < len(cadena):
                cadena = cadena[:pos] + caracteres[i] + cadena[pos + 1:]
                cadenas_modificadas.append(cadena)

        # Ultimo elemento de las cadenas modificadas
        ultima_cadena_modificada = cadenas_modificadas[-1]

        subcadenas_modificadas = [ultima_cadena_modificada[i:i+5] for i in range(0, len(ultima_cadena_modificada), 2) if i+5 <= len(ultima_cadena_modificada)]

        # Lista para almacenar los cambios en cada subcadena modificada
        self.subcadenas_duplicadas_modificadas = []

        # Generar las subcadenas duplicadas con las modificaciones aplicadas
        for i, (subcadena_modificada, subcadena_original) in enumerate(zip(subcadenas_modificadas, subcadenas)):
            time.sleep(.01) #Añade mas tiempo para comprobar de mejro manera el tiempo
            cambios_subcadena = []
            cantidad_modificaciones = sum(1 for a, b in zip(subcadena_modificada, subcadena_original) if a != b)
            for j in range(cantidad_modificaciones + 1):
                subcadena_duplicada_modificada = subcadena_original[:j] + subcadena_modificada[j:]
                cambios_subcadena.append(subcadena_duplicada_modificada)
            self.subcadenas_duplicadas_modificadas.append(cambios_subcadena)

        # Imprimir las subcadenas duplicadas con las modificaciones aplicadas
        self.text_widget.insert(tk.END, "Subcadenas:\n")
        id_subcadena = 1
        for i, cambios_subcadena in enumerate(self.subcadenas_duplicadas_modificadas):
            time.sleep(.01) #Añade mas tiempo para comprobar de mejro manera el tiempo
            self.text_widget.insert(tk.END, f"\nSubcadena original: {id_subcadena}. {subcadenas[i]}\n")
            id_subcadena_modificada = 1
            for j, subcadena in enumerate(cambios_subcadena):
                self.text_widget.insert(tk.END, f"Subcadena modificada {id_subcadena}.{id_subcadena_modificada}: {subcadena}\n")
                id_subcadena_modificada += 1
            id_subcadena += 1

        # Imprimir todas las cadenas modificadas
        self.text_widget.insert(tk.END, "\nTodas las cadenas modificadas:\n")
        for i, cadena_modificada in enumerate(cadenas_modificadas):
            time.sleep(.01) #Añade mas tiempo para comprobar de mejro manera el tiempo
            self.text_widget.insert(tk.END, f"Cadena {i+1}: {cadena_modificada}\n\n")

        # Almacenar las cadenas modificadas
        self.cadenas_modificadas = cadenas_modificadas

        # Calcular el tiempo de ejecución
        end_time = time.time()
        execution_time = end_time - start_time

        # Mostrar el tiempo de ejecución en la etiqueta correspondiente
        self.label_execution_time.config(text=f"Tiempo de ejecución: {execution_time:.4f} segundos")

    def generar_csv(self):
        if not hasattr(self, 'subcadenas_duplicadas_modificadas'):
            self.text_widget.insert(tk.END, "Primero debes realizar las modificaciones antes de generar el CSV.\n")
            return

        # Obtener el nombre del archivo del widget Text
        filename = self.label_selected_name.get("1.0", "end-1c")

        # Determinar la longitud máxima de las listas de subcadenas
        max_length = max(len(subcadenas) for subcadenas in self.subcadenas_duplicadas_modificadas)

        # Rellenar las listas de subcadenas con valores nulos para igualar la longitud
        subcadenas_duplicadas_modificadas_filled = [subcadenas + [''] * (max_length - len(subcadenas)) for subcadenas in self.subcadenas_duplicadas_modificadas]

        # Crear un diccionario para almacenar las columnas de cada subcadena
        columnas = {}
        for i, cambios_subcadena in enumerate(subcadenas_duplicadas_modificadas_filled):
            columna = [f"{i+1}. {subcadena}" for subcadena in cambios_subcadena]
            columnas[f"Subcadena {i+1}"] = columna

        # Guardar los datos en un archivo CSV usando pandas
        df = pd.DataFrame(columnas)
        df.to_csv(f"{filename}.csv", index=False)

        self.text_widget.insert(tk.END, f"Se ha guardado correctamente en '{filename}.csv'.\n")
    
    def combine_substrings(self):
        # Obtener las subcadenas ingresadas por el usuario
        subcadena1 = self.entry_selected_substr1.get()
        subcadena2 = self.entry_selected_substr2.get()

        # Realizar la combinación de las subcadenas
        self.combined_substring = subcadena1 + subcadena2

    def show_combination(self):
        # Verificar si la combinación de subcadenas se ha realizado previamente
        if hasattr(self, 'combined_substring'):
            # Mostrar la combinación en el widget de texto
            self.text_widget.insert(tk.END, f"\nCombinación de subcadenas: {self.combined_substring}\n")
        else:
            # Mostrar un mensaje de error si la combinación no se ha realizado
            self.text_widget.insert(tk.END, "Primero combina las subcadenas antes de mostrar la combinación.\n")
    
    def show_substring(self):
        id_subcadena1 = self.entry_selected_substr1.get()
        id_subcadena2 = self.entry_selected_substr2.get()

        self.subcadenas_mostradas = self.show_subcadena_by_id(id_subcadena1, id_subcadena2)

    def show_subcadena_by_id(self, id_subcadena1, id_subcadena2):
        try:
            id_subcadena1 = int(id_subcadena1)
            id_subcadena2 = int(id_subcadena2)
            if 1 <= id_subcadena1 <= len(self.subcadenas_duplicadas_modificadas) and 1 <= id_subcadena2 <= len(self.subcadenas_duplicadas_modificadas):
                subcadenas1 = self.subcadenas_duplicadas_modificadas[id_subcadena1 - 1]
                subcadenas2 = self.subcadenas_duplicadas_modificadas[id_subcadena2 - 1]
                subcadenas_mostradas = []
                for subcadena in subcadenas1:
                    subcadenas_mostradas.append(subcadena)
                for subcadena in subcadenas2:
                    subcadenas_mostradas.append(subcadena)
                self.text_widget.delete('1.0', tk.END)  # Limpiar el widget de texto
                self.text_widget.insert(tk.END, f"Subcadenas combinadas:\n")
                for subcadena in subcadenas_mostradas:
                    self.text_widget.insert(tk.END, f"{subcadena}\n")
                return subcadenas_mostradas
            else:
                self.text_widget.delete('1.0', tk.END)  # Limpiar el widget de texto
                self.text_widget.insert(tk.END, f"No se encontró ninguna subcadena con el ID {id_subcadena1}\n")
                self.text_widget.insert(tk.END, f"No se encontró ninguna subcadena con el ID {id_subcadena2}\n")
        except ValueError:
            self.text_widget.delete('1.0', tk.END)  # Limpiar el widget de texto
            self.text_widget.insert(tk.END, f"El ID de la subcadena debe ser un número entero\n")

    def combine_and_show_substrings(self):
        if hasattr(self, 'subcadenas_mostradas'):
            combinacion = ''.join(self.subcadenas_mostradas)
            self.text_widget.insert(tk.END, f"\nCombinación de subcadenas: {combinacion}\n")
            print("\nCombinación de subcadenas: ", combinacion)
    
   


if __name__ == "__main__":
    root = tk.Tk()
    app = EditarCadenaApp(root)
    root.mainloop()
