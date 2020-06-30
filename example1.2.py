# -*- coding: utf-8 -*-

import serial
import time

#seri baglanti port ve baud hizi tanimlama
ser=serial.Serial('/dev/ttyS1',9600)

#her okuma ve yazma oncesi input tamponunu temizle
ser.flushInput( )

#seri baglanti ile write-read komutu byte veri gonderir. string gondermek  icin b'' kullanilir.
ser.write(b'\nMerhaba Lutfen [y] veya [n] karakterlerinden birini tuslayiniz: ')
print ("Seri Haberlesme basliyor\n")

while 1:
        ser.flushInput()
        #alinan veriyi byte'dan string'e cevirir. decode()
        karakter=ser.read().decode()
        if karakter ==       'y':
                print ("\nYes denildi\n")
                ser.flushInput()
                ser.write( b'\n[y] karakterini tusladiniz\n')
        elif karakter == "n":
                print ("\nNo denildi\n")
                ser.flushInput()
                ser.write(b'\n[n] karakterini tusladiniz \n')
        else:
                print ("\nbelirlenemeyen bir karakter girisi\n")
                ser.flushInput()
                ser.write(b'\nGirilen karakter =>')
                ser.flushInput()
                #karakter degiskeni str bir degisken. byte gonderim icin encode() kullanilir.
                ser.write(karakter.encode())
                ser.flushInput()
                ser.write(b'\nKarakter belirlenemedigi icin cevap alinmadi. [y]veya [n] karakterlerinden birini girin\n')
        time.sleep(0.1)

