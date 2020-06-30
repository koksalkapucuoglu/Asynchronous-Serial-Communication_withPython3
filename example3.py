import serial
import time


from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PD14
fan = port.PC4

gpio.init()
gpio.setcfg(led,gpio.OUTPUT)
gpio.setcfg(fan,gpio.OUTPUT)

ser=serial.Serial('/dev/ttyS1',9600)
ser.flushInput()
ser.write(b'\nEv Otomasyonu Uygulamasina Hosgeldiniz\n')
print ("Seri Haberlesme basliyor\n")

ser.write(b'\nYapmak istediginiz islemi seciniz\n-\n-->lambayak\n-->lambasondur\n-->kli$

while 1:
        ser.flushInput()
        ser.write(b"\nGirilen islem=> ")
        secenek = ser.readline().decode()

# print ' '.join(format(x, 'b') for x in bytearray(secenek)) #BINARY karsiligi

        if secenek == 'lambayak\r\n':
                gpio.output(led,1)
        elif secenek == "lambasondur\r\n":
                gpio.output(led,0)
        elif secenek == "klimaac\r\n":
                gpio.output(fan,1)
        elif secenek == 'klimakapat\r\n':
                gpio.output(fan,0)
        elif secenek == 'tumkapat\r\n':
                gpio.output(led,0)
                gpio.output(fan,0)
        elif secenek == 'komutlar\r\n':
                ser.write(b'-\n-->lambayak\n-->lambasondur\n-->klimaac\n-->klimakapat\n$
        elif secenek == 'programkapat\r\n':
                ser.write(b'Program kapatiliyor...')
                time.sleep(0.5)
                ser.write(b'\nProgram kapatildi!')
                break

        else:
                ser.write(b'\nGecersiz bir islem girdiniz!!\n')
                ser.write(b'Sadece listede olan islemleri yapabilirsiniz.\n')

        if gpio.input(led) == 1 and gpio.input(fan) == 0:
                ser.write(b"\nLamba Durumu: Acik\n")
                ser.write(b"Klima Durumu : Kapali\n")
                print("Lamba Durumu: Acik\n")
                print("Klima Durumu : Kapali\n")
                print("-\n")
        elif gpio.input(led) == 0 and gpio.input(fan) == 1:
                ser.write(b"\nLamba Durumu: Kapali\n")
                ser.write(b"Klima Durumu : Acik\n")
                print("Lamba Durumu: Kapali\n")
                print("Klima Durumu : Acik\n")
                print("-\n")

        elif gpio.input(led) == 1 and gpio.input(fan) == 1:
                ser.write(b"\nLamba Durumu: Acik\n")
                ser.write(b"Klima Durumu : Acik\n")
                print("Lamba Durumu: Acik\n")
                print("Klima Durumu : Acik\n")
                print("-\n")

        else:
                ser.write(b"\nLamba Durumu: Kapali\n")
                ser.write(b"Klima Durumu : Kapali\n")
                print("Lamba Durumu: Kapali\n")
                print("Klima Durumu : Kapali\n")
                print("-\n")


