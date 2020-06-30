python-serial yas ve burc bulma
#----------------------------------
# -*- coding: utf-8 -*-

import serial
import time

ser=serial.Serial('/dev/ttyS1',9600)
ser.write('\n2 kategorimizi var.Bunlardan birini seciniz\n1-)Yas hesaplama\n2-)burcunuzun ogrenin')
print ("Seri Haberlesme basliyor\n")
while 1:
        ser.write('\n\nLutfen bir kategori secin: ')
        secenek=ser.read()

        if secenek == '1':
                print ("\nYas hesaplama kategorisi secildi\n")
                ser.write( '\ndogum yilinizi giriniz: ')
                yil=ser.read(4)
                intyil=int(yil)
                yas=int(2018-intyil)
                print(yas)
                ser.write('\nyasiniz: ')
                ser.write(str(yas).encode('ascii'))

        elif secenek== "2":
                print("\n Burc kategorisi secildi\n")
                ser.write( '\ndogdugunuz tarihi ay gun bitisik olarak  giriniz: ')
                tarih=ser.readline()
                inttarih=int(tarih)
                if 122 <= inttarih <= 219:
                        burc= 'Kova'
                elif 220 <= inttarih <= 320:
                        burc= 'Balik'
                elif 321 <= inttarih <= 420:
                        burc= 'Koc'
                elif 421 <= inttarih <= 521:
                        burc= 'Boga'
                elif 521 <= inttarih <= 622:
                        burc= 'Ikizler'
                elif 623 <= inttarih <= 722:
                        burc= 'Yengec'
                elif 723 <= inttarih <= 822:
                        burc= 'Aslan'
                elif 823 <= inttarih <= 922:
                        burc= 'Basak'
                elif 923 <= inttarih <= 1022:
                        burc= 'Terzi'
                elif 1023 <= inttarih <= 1121:
                        burc= 'Akrep'
                elif 1122 <= inttarih <= 1221:
                        burc= 'Yay'

                else:
                        burc= 'Oglak'
                print(burc)
                ser.write('\nburcunuz: ')
                ser.write(burc)

        else:
                print( "\nSadece 2 kategorimiz var.\n1-)Yas hesaplama\n2-)Burcunuzu ogrenin\n")


 		ser.write('\nSadece 2 kategorimiz var.\n1-)Yas hesaplama\n2-)Burcunuzu ogrenin\n')
                ser.write('Lutfen bir kategori seciniz\n')

        time.sleep(0.1)


