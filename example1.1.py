# -*- coding: utf-8 -*-

import serial
import time

ser=serial.Serial('/dev/ttyS1',9600)
ser.flushInput( )
ser.write(b'\nMerhaba Lutfen [y] veya [n] karakterlerinden birini tuslayiniz: ')
print ("Seri Haberlesme basliyor\n")

while 1:
        ser.flushInput()
        #strip():izleyen yeni satiri kaldirir.
        karakter=ser.read().strip()
        #decode('ascii'): byte veriyi string'e donusturur.
        strkarakter = karakter.decode('ascii')
        if strkarakter == 'y':
                print ("\nYes denildi\n")
                ser.flushInput()
                ser.write( b'\n[y] karakterini tusladiniz\n')
        elif strkarakter == "n":
                print ("\nNo denildi\n")
                ser.flushInput()
                ser.write(b'\n[n] karakterini tusladiniz \n')
        else:
                print ("\nbelirlenemeyen bir karakter girisi\n")
                ser.flushInput()
                ser.write(b'\nGirilen karakter =>')
                ser.flushInput()
                ser.write(karakter)
                ser.flushInput()
                ser.write(b'\nKarakter belirlenemedigi icin cevap alinmadi. [y]veya [n] karakterlerinden birini girin\n')
        time.sleep(0.1)

