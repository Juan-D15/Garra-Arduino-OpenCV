import serial

class ComunicacionSerial:
    def __init__(self):
        self.com = serial.Serial("COM3", 9600, write_timeout=15) #Puerto del Arduino (COMX), frecuencia de comunicación serial(9600)
    
    def sending_data(self, command: str) -> None:
        self.com.write (command.encode('ascii'))
        print(f'DATA: {command}')