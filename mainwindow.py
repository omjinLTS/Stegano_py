import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import binascii

form_class = uic.loadUiType("Stepyno.ui")[0]
jpgF = ""
hideF = ""

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fileButton_jpg.clicked.connect(self.jpgButtonClicked)
        self.fileButton_hide.clicked.connect(self.hideButtonClicked)
        self.startButton.clicked.connect(self.startButtonClicked)
        self.actionInstruction.triggered.connect(self.actionInstructionClicked)

    def jpgButtonClicked(self):
        global jpgF
        jpgF = QFileDialog.getOpenFileName(self)
        self.jpgLabel.setText(jpgF[0])
        

    def hideButtonClicked(self):
        global hideF
        hideF = QFileDialog.getOpenFileName(self)
        self.hideLabel.setText(hideF[0])
        

    def startButtonClicked(self):
        global jpgF
        global hideF
        mode = self.comboBox.currentText()
        if mode == "Hide":
            try :
                with open(jpgF[0], "rb") as file1:
                    with open(hideF[0], "rb") as file2:
                        with open("secured.jpg", "wb") as file3:
                            original = file1.read()
                            hiding = file2.read()
                            hexhiding = binascii.b2a_hex(hiding)
                            file3.write(original)
                            
                            file3.write(binascii.a2b_hex("ffd9".encode("ascii")+hexhiding))

                QMessageBox.about(self, "Hiding mode","File Successfully Hided")
            except:
                QMessageBox.about(self, "Hiding mode","Error occured")

        elif mode == "Extract Hidden File":
            try:
                with open("Found", "wb") as file1:
                    with open(jpgF[0], "rb") as file2:
                        string = file2.read()
                        hexString = binascii.b2a_hex(string)
                        a = 0
                    while(a % 2 != 1):
                        b = a+1
                        a = hexString[b:].index("ffd9ffd9".encode("ascii"))
                        a = a+b+1
                  
                    a+=7
                    file1.write(binascii.a2b_hex(hexString[a:]))

                QMessageBox.about(self, "Extracting mode","File Successfully Extracted")
            except:
                QMessageBox.about(self, "Extracting mode","Error occurred.\nPlease use .jpg file")

    def actionInstructionClicked(self):
        QMessageBox.about(self, "Instruction",
"""
#To Hide File in Image File
1. Click "Load Image File(jpg)" Button to select image file.
2. Click "Load File to hide" Button to select file to hide.
3. Select "Hide" on combobox, click "Start" Button.
4. New image file conceiling hidden file will be saved in
   same route image file exists as name "secured.jpg"

#To Extract Hidden File from Image File
1. Click "Load Image File(jpg)" Button to select image file.
2. Select "Extract Hidden File" on combobox, click "Start" Button.
3. New image file conceiling hidden file will be saved in
   same route image file exists as name "Found"
4. To open the file you shoud know original file name extention
   ex)If you concealed .zip file : "Found" -> "Found.zip"

""")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
