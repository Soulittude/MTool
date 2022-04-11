import sys
import screen_brightness_control as sbc
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QSlider
from PyQt5.QtCore import Qt, pyqtSlot

class Uygulama(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "MTool v0.1"
        self.left = 500
        self.top = 250
        self.width = 500
        self.height = 350

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Butonke', self)
        button.setToolTip('Bunu yazan tosun, okuyana kosun')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        mySlider = QSlider(Qt.Horizontal, self)
        mySlider.setGeometry(30, 40, 200, 30)
        mySlider.valueChanged[int].connect(self.changeValue)
        
        self.show()

    def changeValue(self, value):
        sbc.set_brightness(value)
        print(value)

    @pyqtSlot()
    def on_click(self):
        sbc.set_brightness(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())   