import time
import serial


class ArduinoController:
    """ Class to connect to an arduino """
    def __init__(self, device, baud_rate, timeout=0.015):
        self.connection = serial.Serial(device, baud_rate, timeout=timeout)
        # sleeps a little bit since the arduino restarts after beginning serial
        # connection and we need to wait a little bit in order for it to read
        # data sent
        time.sleep(2)

    def write(self, msg):
        """ sends data to the arduino """
        if self.connection.is_open():
            self.connection.write(msg.encode("ascii"))

    def read(self):
        """ Reads data from the serial connection """
        if self.connection.isOpen():
            data = self.connection.readline()
            return data

    def stop(self):
        if self.connection.isOpen():
            self.connection.readline()


if __name__ == "__main__":
    device = "/dev/ttyACM0"
    baud_rate = 38400
    arduino = ArduinoController(device, baud_rate)
