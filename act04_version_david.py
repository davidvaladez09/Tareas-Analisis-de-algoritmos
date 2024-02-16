import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput


class CSVLoaderApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        
        self.file_chooser = FileChooserListView()
        self.root.add_widget(self.file_chooser)
        
        load_button = Button(text="Cargar archivo CSV", size_hint=(None, None), size=(200, 50))
        load_button.bind(on_press=self.load_csv)
        self.root.add_widget(load_button)

        generar_csv = Button(text="Generar archivo CSV", size_hint=(None, None), size=(200, 50))
        generar_csv.bind(on_press=self.load_csv)
        self.root.add_widget(generar_csv)
        
        self.info_label = Label(text="")
        self.root.add_widget(self.info_label)
        
        return self.root

    def load_csv(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            selected_file = selected_file[0]
            self.df = pd.read_csv(selected_file)  # Leer archivo CSV con Pandas

            self.show_popup()

    def show_popup(self):
        content = BoxLayout(orientation='vertical')
        popup = Popup(title='Select Cell', content=content, size_hint=(None, None), size=(300, 200))
        
        row_label = Label(text="Row:")
        content.add_widget(row_label)
        self.row_input = TextInput()
        content.add_widget(self.row_input)
        
        col_label = Label(text="Column:")
        content.add_widget(col_label)
        self.col_input = TextInput()
        content.add_widget(self.col_input)
        
        select_button = Button(text="Select Cell", size_hint=(None, None), size=(150, 50))
        select_button.bind(on_press=self.select_cell)
        content.add_widget(select_button)
        
        popup.open()

    def recorridoCadena(self, cadena, longitud_subcadena, inicio_subcadena):
        subcadenas = []
        for i in range(inicio_subcadena, len(cadena), longitud_subcadena):
            subcadenas.append(cadena[i:i+longitud_subcadena])
        return subcadenas

    def modificarCaracter(self, cadena, posicion, nuevo_caracter):
        if posicion < len(cadena):
            cadena = cadena[:posicion] + nuevo_caracter + cadena[posicion+1:]
            return cadena
        else:
            return cadena
    
    def generarCsv(subcadenas):
        df = pd.DataFrame(subcadenas, columns=["Subcadenas"])

        # Guardar el DataFrame en un archivo CSV
        df.to_csv("archivo.csv", index=False)

    def select_cell(self, instance):
        row = self.row_input.text
        col = self.col_input.text

        try:
            row = int(row) - 1  # Ajustar el índice de fila
            col = int(col) - 1  # Ajustar el índice de columna

            if row < 0 or row >= len(self.df) or col < 0 or col >= len(self.df.columns):
                raise ValueError

            cell_data = self.df.iloc[row, col]  # Acceder a los datos con los índices ajustados
            self.info_label.text = f"Celda Seleccionada: {cell_data}"

            # Muestra en consola
            print(cell_data)

            cadena = str(cell_data)
            lista_posicion = self.df['posicion'].tolist()
            lista_referencia = self.df['referencia'].tolist()
            lista_alteracion = self.df['alteracion'].tolist()

            longitud_subcadena = 10
            inicio_subcadena = 0

            subcadenas = self.recorridoCadena(cadena, longitud_subcadena, inicio_subcadena)
            cadenas_modificadas = [cadena]
            modificaciones = []

            # Realizar operaciones con subcadenas y cadenas modificadas

            for i in range(len(lista_posicion)):
                posicion_modificar = lista_posicion[i]
                nuevo_caracter = lista_alteracion[i]

                cadena_modificada = self.modificarCaracter(cadenas_modificadas[-1], posicion_modificar, nuevo_caracter)
                cadenas_modificadas.append(cadena_modificada)

                print("Cadena modificada:", cadena_modificada)


            print('\n')

            print("Cadenas modificadas:", '\n'.join(cadenas_modificadas))
            cadenas_modificadas_texto = "\n".join(cadenas_modificadas)
            subcadenas_texto = "\n".join(subcadenas)
            self.info_label.text = f"Cadenas modificadas: {cadenas_modificadas_texto}\nSubcadenas: {subcadenas_texto}"


        except ValueError:
            self.info_label.text = "Las filas o columnas no son validas."


if __name__ == "__main__":
    CSVLoaderApp().run()
