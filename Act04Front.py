import csv
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CSVLoader(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Creamos un botón para cargar el archivo CSV
        self.btn_load_csv = Button(text="Cargar archivo CSV", size_hint=(None, None), size=(200, 50))
        self.btn_load_csv.bind(on_press=self.load_csv)
        
        # Creamos una etiqueta para mostrar el valor de la celda
        self.label_value = Label(text="", size_hint=(None, None), size=(200, 50))
        
        self.layout.add_widget(self.btn_load_csv)
        self.layout.add_widget(self.label_value)
        
        return self.layout

    def load_csv(self, instance):
        # Abre un dialogo para seleccionar el archivo
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()  # Oculta la ventana principal de tkinter
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        
        if file_path:
            # Si se selecciona un archivo, lo cargamos
            with open(file_path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                # Leemos el valor de la primera celda de la primera fila
                try:
                    value = next(csvreader)[0]
                    # Actualizamos el texto de la etiqueta con el valor de la celda
                    self.label_value.text = value
                except StopIteration:
                    # Si el archivo CSV está vacío, mostramos un mensaje de error en la etiqueta
                    self.label_value.text = "El archivo CSV está vacío"

if __name__ == '__main__':
    CSVLoader().run()
