import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import time
import matplotlib.pyplot as plt

class EdicionCadenasApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        
        #Muestra el explorar de archivos dentro de la ventana
        self.file_chooser = FileChooserListView()
        self.root.add_widget(self.file_chooser)
        
        #Boton que cargar llama a la funcion que carga el archivo csv
        button_cargar_csv = Button(text="Cargar archivo CSV", size_hint=(None,None), size=(200, 50))
        button_cargar_csv.pos_hint = {'center_x': 0.5}
        button_cargar_csv.bind(on_press=self.cargarCsv)
        self.root.add_widget(button_cargar_csv)
        
        self.info_label = Label(text="")
        self.root.add_widget(self.info_label)
        
        return self.root

    #Funcion que carga el archivo csv 
    def cargarCsv(self, instance):
        archivo = self.file_chooser.selection
        if archivo:
            archivo = archivo[0] #Se coloca el archivo en la posicion 0 de una lista en caso de que se selccione mas de un archivo
            self.df = pd.read_csv(archivo) #Lee el archivo csv

            self.show_popup_seleccionar_celda() #Manda a llamar a la funcion para seleecionar la celda

    #Funcion para solicitar al usuario celda de cadena a editar
    def show_popup_seleccionar_celda(self):
        contenido_seleccionar_celda = BoxLayout(orientation='vertical')
        popup = Popup(title='Seleccionar Celda Cadena a Editar', content=contenido_seleccionar_celda, size_hint=(None, None), size=(300, 250))
        
        #Label para ingresar fila
        label_fila = Label(text="Fila:")
        contenido_seleccionar_celda.add_widget(label_fila)
        self.label_fila = TextInput(size_hint_y=None, height=40)
        contenido_seleccionar_celda.add_widget(self.label_fila)
        
        #Label para ingresar columna
        label_columna = Label(text="Columna:")
        contenido_seleccionar_celda.add_widget(label_columna)
        self.label_columna = TextInput(size_hint_y=None, height=40)
        contenido_seleccionar_celda.add_widget(self.label_columna)
        
        #Boton que selecciona la celda con la fila y columna ingresada
        button_seleccionar_celda = Button(text="Seleccionar Celda", size_hint=(None, None), size=(150, 50))
        button_seleccionar_celda.pos_hint = {'center_x': 0.5}
        button_seleccionar_celda.bind(on_press=self.seleccionar_celda)
        contenido_seleccionar_celda.add_widget(button_seleccionar_celda)
        
        popup.open()
    
    #Funcion que recorre la cadena de la cela seleccionada 
    def recorridoCadena(self, cadena, longitud_subcadena, inicio_subcadena):
        subcadenas = [] #Lista para almacenar todas las subcadenas generadas
        for i in range(inicio_subcadena, len(cadena), longitud_subcadena): #Itera en la lista principal, inicia en una subcadena y toma la longitud de la cadena 
            subcadenas.append(cadena[i:i+longitud_subcadena]) #Ingresa las subcadenas en la lista
        return subcadenas #Retorna la lsita de subcadsenas

    #Funcion que modifica las posiciones de la cadena original 
    def modificarCaracter(self, cadena, posicion, nuevo_caracter): #Recibe la cadena original, la posicion a modificar y el nuevo caracter
        if posicion < len(cadena): #Encontra la poscion en la cadena
            cadena = cadena[:posicion] + nuevo_caracter + cadena[posicion+1:] #Modifica la posicion si la encuentra
            return cadena #Regresa la cadena
        else:
            return cadena
        
    #Funcion para generar el archivo csv 
    def generarCsv(self, filename, cadenas_modificadas, subcadenas): #Recibe la lista de subcadenas y lista de modificaciones
        #Encuentra la longitud maxima de las listas recibidas para poder generar el archivo
        longitud_maxima = max(len(cadenas_modificadas), len(subcadenas))

        #Si las lsiatas son de diferente longitud complementa las listas con elementos faltantes con None
        cadenas_modificadas_completa = cadenas_modificadas + [None] * (longitud_maxima - len(cadenas_modificadas))
        subcadenas_completa = subcadenas + [None] * (longitud_maxima - len(subcadenas))

        if filename: #Si el nombre del archivo es correcto en la funcion nombre_archivo_popup
            df = pd.DataFrame({'Cadenas_modificadas': subcadenas_completa, 'Subcadenas': cadenas_modificadas_completa}) #Crea un dataframe para el archivo
            df.to_csv(f"{filename}.csv", index=False) #Crear archivo csv
            self.info_label.text = f"Archivo '{filename}.csv' generado y guardado exitosamente." #Muestra mensaje de que el archivo se ha generado correctamente
        else:
            self.info_label.text = "Nombre de archivo no valido."

    #Funcion para solicitar al usuario el nombre del archivo a generar
    def nombre_archivo_popup(self, subcadenas, cadenas_modificadas):
        contenido_nombre_archivo = GridLayout(cols=1, padding=10)
        
        #Label para el nombre del archivo
        input_nombre_archivo = TextInput(hint_text='Nombre del archivo CSV', multiline=False)
        contenido_nombre_archivo.add_widget(input_nombre_archivo)
        
        #Boton para guaradar el archivo
        button_guardar_archivo = Button(text="Guardar archivo", size_hint=(None, None), size=(200, 50))
        button_guardar_archivo.pos_hint = {'center_x': 0.5}
        button_guardar_archivo.bind(on_press=lambda _: self.generarCsv(input_nombre_archivo.text, cadenas_modificadas, subcadenas))
        contenido_nombre_archivo.add_widget(button_guardar_archivo)
        
        popup = Popup(title='Guardar archivo CSV', content=contenido_nombre_archivo, size_hint=(None, None), size=(300, 200))
        popup.open()

    #Funcion que selecciona que define la celda con la que contiene la cadena a modificar y realiza las modificaciones de las posiciones por la alteracion
    def seleccionar_celda(self, instance):
        #Obtiene la fila y columna del label del poppup
        fila = self.label_fila.text
        columna = self.label_columna.text

        try: 
            #Se ajusta el indice de la fila y columna
            fila_ajuste = int(fila) - 1 
            columna_ajuste = int(columna) - 1  

            if fila_ajuste < 0 or fila_ajuste >= len(self.df) or columna_ajuste < 0 or columna_ajuste >= len(self.df.columns):
                raise ValueError

            cadena = self.df.iloc[fila_ajuste, columna_ajuste]  #Define la variable con las celdas seleccionadas por el usuario
            self.info_label.text = f"Celda Seleccionada: {cadena}" #Muestra la celda que se selecciono 

            lista_posicion = self.df['posicion'].tolist() #Todos los elementos de la columna posicion los ingresa a una lista
            lista_alteracion = self.df['alteracion'].tolist() #Todos los elementos de la columna alteracion los ingresa a una lista

            #Define la longitud de la subcadena  y el inicio de la misma
            longitud_subcadena = 10
            inicio_subcadena = 0

            subcadenas = self.recorridoCadena(cadena, longitud_subcadena, inicio_subcadena) #Inicializa con el resultado de la funcion recorridoCadena que retorna la lista de las subcadenas
            cadenas_modificadas = [cadena] #Inicializa con la lista de la cadena original

            for i in range(len(lista_posicion)): #Itera sobre en la lista de lista_posicion
                posicion_modificar = lista_posicion[i] #Accede al caracter de lista_alteracion que tiene el caracter nuevo que se modificara en esa posicion
                nuevo_caracter = lista_alteracion[i]

                cadena_modificada = self.modificarCaracter(cadenas_modificadas[-1], posicion_modificar, nuevo_caracter) #Modifica en la cadena original toma como parametro la cadena original
                cadenas_modificadas.append(cadena_modificada) #Inserta las cadenas modificadas a la lista

            cadenas_modificadas_texto = "\n".join(cadenas_modificadas) #Convierte la lista en en texto para utilizarlo en la ventana de la aplicacion
            subcadenas_texto = "\n".join(subcadenas) #Convierte la lista en en texto para utilizarlo en la ventana de la aplicacion
            self.info_label.text = f"\n\n\nCadenas modificadas:\n{cadenas_modificadas_texto}\n\nSubcadenas:\n{subcadenas_texto}" #Muestra las cadenas en la ventan principal de la aplicacion 

            #Boton que muestra al usuario con que nombre desea guardar el archivo
            button_csv = Button(text="Generar archivo CSV", size_hint=(None,None), size=(200, 50))
            button_csv.pos_hint = {'center_x': 0.5}
            button_csv.bind(on_press=lambda instance: self.nombre_archivo_popup(cadenas_modificadas, subcadenas))
            self.root.add_widget(button_csv)

        except ValueError:
            self.info_label.text = "Las filas o columnas no son validas."

if __name__ == "__main__":
    lista_tiempos = []
    
    while True:
        opcion = input('Desea continuar(si/no): ')

        if opcion != 'si':
            break

        tiempoInicio = time.time()

        EdicionCadenasApp().run()

        tiempoFin = time.time()

        tiempoEjecucion = tiempoFin - tiempoInicio
        lista_tiempos.append(tiempoEjecucion)

    plt.plot(lista_tiempos)
    plt.xlabel('Ejecución')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de ejecución por ejecución')
    plt.show()
