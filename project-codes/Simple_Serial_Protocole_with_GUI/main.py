from ssp import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from time import sleep

import sys
import time
import serial
import serial.tools
import serial.tools.list_ports

app = QtWidgets.QApplication([])
dlg = uic.loadUi("RoverTry.ui")
dlg1 = uic.loadUi("photo.ui")

# SSP parameters
x = []
resp = []
ser = None
data_sent = [6, 77, 8, 9, 0x44, 0x33, 0x11, 0x44, 6, 6, 6, 6, 77, 8, 9]
header = [0xA, 0xB, 5, 0x0f]
z = ssp_construction(bytearray(header), bytearray(data_sent), len(data_sent))
type_num = response(bytearray(header), bytearray(data_sent), bytearray(resp))

x.append(27)
x.append(15)
x.append(57)
x.append(27)
x.extend(z)
data = data_extraction(bytearray(x), len(x))
print(f"\nz: {z}")
print(f"\nthe wrong frame x: {x}")
print(f"\ndata: {data}")
print(f"\ntype_num: {type_num}")


def serial_ports():
    ports = serial.tools.list_ports.comports()
    i = 0
    a_port = []
    global ser
    # gui_port = dlg.comboBox_4.currentText()
    # ser = serial.Serial(gui_port, baudrate=9600, timeout=2)
    # ser.flushInput()  # flush input buffer, discarding all its contents
    # ser.flushOutput()  # flush output buffer, aborting current output
    # print(ser.isOpen())
    for port in sorted(ports):
        a_port = port[0]
        check_ports = [dlg.comboBox_4.itemText(index_l) for index_l in range(dlg.comboBox_4.count())]
        if a_port not in check_ports:
            dlg.comboBox_4.addItem(a_port)
            print(a_port)
            i = i + 1
    return a_port


def show_new_window():
    dlg1.show()


def collect():
    if not dlg.lineEdit.text() == "":  # this is for if data is empty do not enter
        comm = dlg.comboBox.currentText()
        baud = dlg.comboBox_2.currentText()
        command = dlg.comboBox_3.currentText()
        index = dlg.comboBox_3.currentIndex()
        sent_data = dlg.lineEdit.text()
        print("\nThis is from UI:")
        print(comm, "-", baud, "-", command)
        print(sent_data)
        dlg.lineEdit_2.setText(str(z))
        dlg.lineEdit_3.setText(str(data))
        dlg.lineEdit_4.setText(str(type_num))
        dlg.lineEdit_5.setText(str(index))

    else:
        show_message("Warning!", "You Have to type in Serial Write")


def show_message(title="Test", message="Test"):
    QMessageBox.information(None, title, message)


if __name__ == '__main__':
    # main

    dlg.pushButton.clicked.connect(collect)  # For Connecting The Push button to the Function you Want
    dlg.pushButton_2.clicked.connect(serial_ports)  # For Connecting The Push button to the Function you Want
    dlg.pushButton_3.clicked.connect(show_new_window)

    dlg.lineEdit_2.setReadOnly(True)  # This is so that the user can not change in the second line
    dlg.lineEdit_3.setReadOnly(True)  # This is so that the user can not change in the second line
    dlg.lineEdit_4.setReadOnly(True)  # This is so that the user can not change in the second line

    dlg.show()
try:
    app.exec()

except serial.SerialException as e:
    print(str(e))
    sys.exit(1)
except TypeError as e:
    print(str(e))
    ser.port.close()
    sys.exit(1)



