from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('converter.ui', None)
        self.ui.show()

        self.weight_list = ['Grams', 'kilograms', 'tons', 'pounds']
        self.length_list = ['Mm', 'cm', 'meter', 'kilometer', 'inch']
        self.temperature_list = ['Celsius', 'Fahrenheit', 'Kelvin']
        self.digital_storage_list = ['Bits', 'bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes']

        self.ui.main_combobox.currentIndexChanged.connect(self.update_ComboBox)
        self.ui.btn_convert.clicked.connect(self.Convert)

    def update_ComboBox(self):
        self.ui.from_combobox.clear()
        self.ui.to_combobox.clear()

        if self.ui.main_combobox.currentText() == 'Weight':
            for item in self.weight_list:
                self.ui.from_combobox.addItem(item)
                self.ui.to_combobox.addItem(item)
        
        elif self.ui.main_combobox.currentText() == 'length':
            for item in self.length_list:
                self.ui.from_combobox.addItem(item)
                self.ui.to_combobox.addItem(item)

        elif self.ui.main_combobox.currentText() == 'Temperature':
            for item in self.temperature_list:
                self.ui.from_combobox.addItem(item)
                self.ui.to_combobox.addItem(item)

        elif self.ui.main_combobox.currentText() == 'Digital storage':
            for item in self.digital_storage_list:
                self.ui.from_combobox.addItem(item)
                self.ui.to_combobox.addItem(item)

    def Convert(self):
        try:
            convert = self.ui.main_combobox.currentText()
            From = self.ui.from_combobox.currentText()
            To = self.ui.to_combobox.currentText()
            inp = float(self.ui.input_text.text())
            
            if convert == 'Weight':
                if From == 'Grams':
                    if To == 'Grams':
                        result = inp
                    elif To == 'kilograms':
                        result = inp / 1000
                    elif To == 'tons':
                        result = inp / 1000000
                    elif To == 'pounds':
                        result = inp * 0.0022
                
                elif From == 'kilograms':
                    if To == 'Grams':
                        result = inp * 1000
                    elif To == 'kilograms':
                        result = inp
                    elif To == 'tons':
                        result = inp / 1000
                    elif To == 'pounds':
                        result = inp * 2.205
                
                elif From == 'tons':
                    if To == 'Grams':
                        result = inp * 1000000
                    elif To == 'kilograms':
                        result = inp * 1000
                    elif To == 'tons':
                        result = inp
                    elif To == 'pounds':
                        result = inp * 2679.2289
                
                elif From == 'pounds':
                    if To == 'Grams':
                        result = inp * 453.59237
                    elif To == 'kilograms':
                        result = inp * 0.45359237
                    elif To == 'tons':
                        result = inp * 0.0004535924
                    elif To == 'pounds':
                        result = inp
            
            elif convert == 'length':
                if From == 'Mm':
                    if To == 'Mm':
                        result = inp
                    elif To == 'cm':
                        result = inp * 0.1
                    elif To == 'meter':
                        result = inp * 0.001
                    elif To == 'kilometer':
                        result = inp * 0.000001
                    elif To == 'inch':
                        result = inp * 0.0394
                
                elif From == 'cm':
                    if To == 'Mm':
                        result = inp * 10
                    elif To == 'cm':
                        result = inp
                    elif To == 'meter':
                        result = inp * 0.01
                    elif To == 'kilometer':
                        result = inp * 0.00001
                    elif To == 'inch':
                        result = inp * 0.3937

                elif From == 'meter':
                    if To == 'Mm':
                        result = inp * 1000
                    elif To == 'cm':
                        result = inp * 100
                    elif To == 'meter':
                        result = inp
                    elif To == 'kilometer':
                        result = inp * 0.001
                    elif To == 'inch':
                        result = inp * 39.3700787

                elif From == 'kilometer':
                    if To == 'Mm':
                        result = inp * 1000000
                    elif To == 'cm':
                        result = inp * 100000
                    elif To == 'meter':
                        result = inp * 1000
                    elif To == 'kilometer':
                        result = inp
                    elif To == 'inch':
                        result = inp * 39370.0787

                elif From == 'inch':
                    if To == 'Mm':
                        result = inp * 25.4
                    elif To == 'cm':
                        result = inp * 2.54
                    elif To == 'meter':
                        result = inp * 0.0254
                    elif To == 'kilometer':
                        result = inp * 0.0000254
                    elif To == 'inch':
                        result = inp

            elif convert == 'Temperature':
                if From == 'Celsius':
                    if To == 'Celsius':
                        result = inp
                    elif To == 'Fahrenheit':
                        result = inp * 9/5 + 32
                    elif To == 'Kelvin':
                        result = inp + 273
            
                elif From == 'Fahrenheit':
                    if To == 'Celsius':
                        result = 5/9 * (inp - 32)
                    elif To == 'Fahrenheit':
                        result = inp
                    elif To == 'Kelvin':
                        x = 5/9 * (inp - 32)
                        result = x + 273
                
                elif From == 'Kelvin':
                    if To == 'Celsius':
                        result = inp - 273
                    elif To == 'Fahrenheit':
                        result = 1.8 * (inp - 273) + 32
                    elif To == 'Kelvin':
                        result = inp

            elif convert == 'Digital storage':
                if From == 'Bits':
                    if To == 'Bits':
                        result = inp
                    elif To == 'bytes':
                        result = inp * 0.125
                    elif To == 'kilobytes':
                        result = inp * (1/8) * 0.001
                    elif To == 'megabytes':
                        result = inp * (1/8) * 10**-6
                    elif To == 'gigabytes':
                        result = inp * (1/8) * 10**-9
                    elif To == 'terabytes':
                        result = inp * (1/8) * 10**-12
                
                elif From == 'bytes':
                    if To == 'Bits':
                        result = inp * 8
                    elif To == 'bytes':
                        result = inp
                    elif To == 'kilobytes':
                        result = inp / 1024
                    elif To == 'megabytes':
                        result = inp / (1024 ** 2)
                    elif To == 'gigabytes':
                        result = inp / (1024 ** 3)
                    elif To == 'terabytes':
                        result = inp / (1024 ** 4)

                elif From == 'kilobytes':
                    if To == 'Bits':
                        result = inp * 8 * 1000
                    elif To == 'bytes':
                        result = inp * 1000
                    elif To == 'kilobytes':
                        result = inp
                    elif To == 'megabytes':
                        result = inp / 1000
                    elif To == 'gigabytes':
                        result = inp / (1000 ** 2)
                    elif To == 'terabytes':
                        result = inp / (1000 ** 3)
                
                elif From == 'megabytes':
                    if To == 'Bits':
                        result = inp * 8 * (1000 ** 2)
                    elif To == 'bytes':
                        result = inp * (1024 ** 2)
                    elif To == 'kilobytes':
                        result = inp * 1000
                    elif To == 'megabytes':
                        result = inp
                    elif To == 'gigabytes':
                        result = inp / 1000
                    elif To == 'terabytes':
                        result = inp / (1000 ** 2)

                elif From == 'gigabytes':
                    if To == 'Bits':
                        result = inp * 8 * (1000 ** 3)
                    elif To == 'bytes':
                        result = inp * (1024 ** 3)
                    elif To == 'kilobytes':
                        result = inp * (1000 ** 2)
                    elif To == 'megabytes':
                        result = inp * 1000
                    elif To == 'gigabytes':
                        result = inp
                    elif To == 'terabytes':
                        result = inp / 1000

                elif From == 'terabytes':
                    if To == 'Bits':
                        result = inp * 8 * (1000 ** 4)
                    elif To == 'bytes':
                        result = inp * (1024 ** 4)
                    elif To == 'kilobytes':
                        result = inp * (1000 ** 3)
                    elif To == 'megabytes':
                        result = inp * (1000 ** 2)
                    elif To == 'gigabytes':
                        result = inp / 1000
                    elif To == 'terabytes':
                        result = inp

            self.ui.output_text.setText(str(result))
            
        except:
            print('Error!')
            pass

app = QApplication([])
window = Converter()
app.exec()