from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QComboBox, QLabel, QBoxLayout, QHBoxLayout
import sys
import serial
from time import sleep
import serial.tools.list_ports as port_com
from PyQt5.QtGui import QPixmap
import time

ser = None
ports = list(port_com.comports())

global size
size = 25
size_crc = 252
Dest = 0xdd
Source = 0xCf
GCS = True
Command = 0x00
Response = 0xc0
SSP_Packet = []
SSP_Packet_Without_CRC = []
data_array = []
for i in range(256):
    data_array.insert(i, 0xd8)

for i in range(264):
    SSP_Packet.insert(i, 0xd8)
SSP_Packet = bytearray(SSP_Packet)
SSP_Packet[0] = 0xc0
SSP_Packet[size + 7] = 0xc0
SSP_Packet[1] = Dest
SSP_Packet[2] = Source
SSP_Packet[4] = size
PNG: int = 0x00
capture_image = 0x0A
command_ID = capture_image
get_humidity = 0x0B
get_temperature = 0x0C
get_heading = 0x0D
get_obstacle_sensors = 0x0E
toggle_scan = 0x0F
get_telemetry = 0x10
get_image_ID = 0x11
servo_angle = 0x12


class GUI(QDialog):
    def __init__(self):
        super(GUI, self).__init__()
        loadUi("GUI (1).ui", self)

        # when button clicked go to send function
        self.sendbutton.clicked.connect(self.combo_selected)
        self.Connect.clicked.connect(self.connect_serial)

        self.DisplayButton.clicked.connect(self.Display_Image)
        self.com_port.addItem('Select Port')
        self.ImageID.addItem('Select ID')
        for p in ports:
            self.com_port.addItem(p[0])
        self.findChild(QComboBox, 'com_port').currentTextChanged.connect(self.combo_selected)
        self.counter = 1

    def Display_Image(self):
        try:
            super(GUI, self).__init__()
            loadUi("DisplayImage.ui", self)
            self.show()
            ID = self.ImageID.currentText()
            if ID == 'Select ID':
                return
            # print(ID)
            if ID == '0':
                print(ID)
                hbox = QHBoxLayout(self)
                pixmap = QPixmap('0.jpg')
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                hbox.addWidget(lbl)
                self.setLayout(hbox)
                self.setWindowTitle('Image')
                self.show()
            if ID == '1':
                print(ID)
                hbox = QHBoxLayout(self)
                pixmap = QPixmap('1.jpg')
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                hbox.addWidget(lbl)
                self.setLayout(hbox)
                self.setWindowTitle('Image')
                self.show()
            if ID == '2':
                print(ID)
                hbox = QHBoxLayout(self)
                pixmap = QPixmap('2.jpg')
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                hbox.addWidget(lbl)
                self.setLayout(hbox)
                self.setWindowTitle('Image')
                self.show()
            if ID == '3':
                print(ID)
                hbox = QHBoxLayout(self)
                pixmap = QPixmap('3.jpg')
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                lbl = QLabel(self)
                lbl.setPixmap(pixmap)
                hbox.addWidget(lbl)
                self.setLayout(hbox)
                self.setWindowTitle('Image')
                self.show()
        except:
            print('cannot display image')

    def connect_serial(self):
        try:
            port = self.com_port.currentText()
            global ser
            ser = serial.Serial(port, baudrate=9600, timeout=2)
            ser.flushInput()  # flush input buffer, discarding all its contents
            ser.flushOutput()  # flush output buffer, aborting current output
            print(ser.isOpen())
        except serial.SerialException as e:
            print(str(e))
            print('Robot Unavailable, connect again!')

    def combo_selected(self):
        item = self.comboBox.currentText()
        try:
            if item == 'Capture Image':
                print("capture Image")
                command_ID = capture_image
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                print("hello")
                self.ack.setText("WAITING!")
                sleep(5)
                if ser.inWaiting() >= 8:
                    sleep(2)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(data_received)
                                    self.ack.setText("ACK Received!")
                                    self.ImageID.addItem(str(self.counter))
                                    self.counter += 1

            if item == 'Temperature':
                print("Get Temperature")
                command_ID = get_temperature
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(15)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(data_received)
                                    self.ack.setText("DATA RECEIVED!")
                                    self.temptextedit.setText(str(data_received))

            if item == 'Humidity':
                print("Get Humidity")
                command_ID = get_humidity
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(15)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(data_received)
                                    self.ack.setText("DATA RECEIVED!")
                                    self.humiditytextedit.setText(str(data_received))

            if item == 'Telemetry':
                print("Get Telemetry")
                command_ID = get_telemetry
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(5)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(data_received)
                                    self.ack.setText("DATA RECEIVED!")
                                    self.metalY.setText(str(data_received[5]))
                                    self.metalX.setText(str(data_received[4]))
                                    self.cputextedit.setText(str(data_received[3]))
                                    self.headingtextedit.setText(str(data_received[2]))
                                    self.postexteditY.setText(str(data_received[1]))
                                    self.postexteditX.setText(str(data_received[0]))

            if item == 'Heading':
                print("Get Heading")
                command_ID = get_heading
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(5)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(data_received)
                                    self.ack.setText("DATA RECEIVED!")
                                    self.headingtextedit.setText(str(data_received))

            if item == 'Obstacle Sensors':
                print("Get Obstacle Sensors")
                command_ID = get_obstacle_sensors
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(5)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(data_received)
                                    self.ack.setText("DATA RECEIVED!")
                                    self.ultratexteditR.setText(str(data_received[0]))
                                    self.ultratexteditL.setText(str(data_received[1]))

            if item == 'Scan':
                print("start scan")
                command_ID = toggle_scan
                data = 0
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(1)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(bytes(data_received))
                                    self.ack.setText("ACK Received!")

            if item == 'Fetch Image':
                print("Get Image ID")
                command_ID = get_image_ID
                data = int(self.ImageID.currentText())
                byte_data = data.to_bytes(2, 'big')
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(5)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print('img size', data_received)
                                    self.ack.setText("ACK Received!")
                                    write_to_file_path = str(data) + '.jpg'
                                    output_file = open(write_to_file_path, "ab")
                                    start_time = time.time()
                                    seconds = 30
                                    while True:
                                        current_time = time.time()
                                        elapsed_time = current_time - start_time
                                        counter = ser.read(256)
                                        output_file.write(counter)
                                        print(counter)
                                        print(time.time())
                                        if elapsed_time > seconds:
                                            print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
                                            break
                                    output_file.flush()
                                    output_file.close()

            if item == 'Cam Angle':
                command_ID = servo_angle
                servo1_string = self.servoangle1.text()
                servo1 = int(servo1_string)
                if servo1 >= 0 & servo1 <= 180:
                    print('Servo Angle=')
                    print(servo1)
                data = servo1
                byte_data = data.to_bytes(2, 'big', signed=True)
                size = len(byte_data)
                print('size', size, 'data', byte_data)
                for i in range(size):
                    data_array[i] = byte_data[i]
                SSP_Pack = check_crc(command_ID, SSP_Packet, SSP_Packet_Without_CRC, size, data_array)
                ser.write(bytearray(SSP_Pack))
                print(bytearray(SSP_Pack))
                self.ack.setText("WAITING!")
                sleep(5)
                if ser.inWaiting() >= 8:
                    sleep(0.025)
                    buffer = ser.read(ser.inWaiting())
                    ser.flushInput()  # flush input buffer, discarding all its contents
                    print(len(buffer), buffer)
                    for idx, i in enumerate(buffer):
                        if idx + 4 < len(buffer):
                            if i == 0xc0 and buffer[idx + buffer[idx + 4] + 7] == 0xc0:
                                print(idx, i)
                                crc_buffer = buffer[idx + 1:idx + buffer[idx + 4] + 7]
                                print(crc_buffer)
                                if checksum_validate(crc_buffer) and check_src_dest(crc_buffer):
                                    print("Source and Destination Verified")
                                    data_received = []
                                    for i in range(crc_buffer[3]):
                                        data_received.insert(i, crc_buffer[i + 4])
                                    print(bytes(data_received))
                                    self.ack.setText("ACK Received!")
        except:
            print('Robot Unavailable, connect again!')


def checksum_validate(packet):
    crc_bytes = packet[len(packet) - 2:len(packet)]
    data_bytes = packet[0:len(packet) - 2]
    print(packet[3], packet)
    size = packet[3]
    print(data_bytes, '\n', crc_bytes)
    crc_clc = ssp2bytecrc(data_bytes, size)
    print('crc', crc_bytes)
    print('data', len(data_bytes), data_bytes)
    print(crc_clc)
    C = crc_clc >> 8
    D = (crc_clc & 0x00ff)
    if crc_bytes[0] == C and crc_bytes[1] == D:
        print("Checksum Passed!")
        return True
    else:
        print("Checksum Error!")
        return False


def check_src_dest(packet):
    if packet[0] == Source and packet[1] == Dest:
        return True


def READ_SERIAL():
    while True:
        sleep(2)


if __name__ == '__main__':
    # main
    app = QApplication(sys.argv)
    gui = GUI()
    widget = QStackedWidget()
    widget.addWidget(gui)
    widget.setFixedHeight(650)
    widget.setFixedWidth(800)
    widget.show()

try:
    app.exec_()

except serial.SerialException as e:
    print(str(e))
    sys.exit(1)
except TypeError as e:
    print(str(e))
    ser.port.close()
    sys.exit(1)
