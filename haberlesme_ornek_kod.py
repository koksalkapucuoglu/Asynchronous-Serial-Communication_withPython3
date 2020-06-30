# -*- coding: utf-8 -*-

import serial
import time

ser=serial.Serial('/dev/ttyS1',9600)
ser.write('\nMerhaba Lutfen [y] veya [n] karakterlerinden birini tuslayiniz: ')
print("Seri Haberlesme basliyor\n")

while 1:
        karakter=ser.read()

        if karakter == 'y':
                print("\nYes denildi\n")
                ser.write( '\n[y] karakterini tusladiniz\n')
        elif karakter == "n":
                print("\nNo denildi\n")
                ser.write('\n[n] karakterini tusladiniz \n')


        else:
                print("\nbelirlenemeyen bir karakter girisi\n")
                ser.write('\nGirilen karakter =>')
                ser.write(karakter)
                ser.write('\nKarakter belirlenemedigi icin cevap alinmadi. [y]veya [n] karakterlerinden birini girin\n')
        time.sleep(0.1)
