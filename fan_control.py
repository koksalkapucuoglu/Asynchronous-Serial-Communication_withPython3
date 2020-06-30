import serial
import time

from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PC4
fan = port.PD14

gpio.init()
gpio.setcfg(led,gpio.OUTPUT)
gpio.setcfg(fan,gpio.OUTPUT)

ser=serial.Serial('/dev/ttyS1',9600)
ser.write('\n2 kategorimiz var.Bunlardan birini seciniz\n1-)1 sn araliklarla led yakma\n2-)fani dondur')
print("Seri Haberlesme basliyor\n")

ser.write('\n\nLutfen bir kategori secin: ')


while 1:

        secenek=ser.read()

        if secenek == '1':
                ser.write("\nLed yaniyor\n")
                for counter in range(5):
                        gpio.output(led,1)
                        time.sleep(1)
                        gpio.output(led,0)
                        time.sleep(1)
                ser.write("\nLed sondu\n")
        elif secenek == '2':
                ser.write("\nFan calisiyor\n ")
                gpio.output(fan,1)
                time.sleep(10)
                gpio.output(fan,0)
                ser.write("\nFan durdu\n")

        else:

                ser.write('\nSadece 2 kategorimiz var.\n1-)1 sn araliklarla led yakma \n2-)fan dondur\n')
                ser.write('Lutfen bir kategori seciniz\n')
                continue

        ser.write('\nBaska bir secim yapabilirsiniz:\n1-)1 sn araliklarla led yakma\n2-)fan dondur\n')
