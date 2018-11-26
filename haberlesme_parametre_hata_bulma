# -*- coding: utf-8 -*-

import serial
import time

ser=serial.Serial(port='/dev/ttyS1',baudrate= 9600,bytesize=serial.EIGHTBITS )
print "Seri Haberlesme basliyor\n"
while 1:
        print "\nMerhaba Lutfen seri ekrana sadece [y] veya [n] karakterlerinden birini giriniz!"
        ser.write('\nMerhaba Lutfen sadece [y] veya [n] karakterlerinden birini giriniz: ')

        karakter=ser.read() #kullanicinin girdigi girdigi karakter

        if karakter == 'y':  # program geregi 'y' veya 'n' denildiginde karsi tarafa bu bildirilir. Diger durumlarda yanlis giris olur.
                print "\nYes denildi\n"
                ser.write( '\n[y] karakterini tusladiniz \n')
        elif karakter == "n":
                print "\nNo denildi\n"
                ser.write('\n[n] karakterini tusladiniz \n')


        else:
                print "\nbelirlenemeyen bir karakter girisi\n" # program geregi yanlis girislerde uyarı mesaji verilir.
                karakter_int = ord(karakter) #girilen karakter ASCII koduna donusturulur.
                if karakter_int > 128:
                        sayi1 = karakter_int - 128  # veri bitinin pc:orangepi = 7bit:8bit olması durumunda MSB biti 0 iken 1 okunuyordu. Verinin asıl hal için 128 çıkarırız.
                        print "\nOrange pi'ye gelen karakter ve bilgileri\n--------------------\n"
                        print karakter
                        print "\nASCII "
                        print (karakter_int) #ASCIIl karsiligi ilk yol
                        #print reduce(lambda x, y: str(x)+str(y), map(ord,karakter)) #ASCII karsiligi ikinci yol
                        print "\nHEX"
                        print list(bytes(karakter)) #HEX karsiligi
                        print "\nBINARY"
                        print ' '.join(format(x, 'b') for x in bytearray(karakter)) #BINARY karsiligi
                        #a=' '.join(format(x, 'b') for x in bytearray(karakter))
                        #print a   #Binary karsiligi bir degiskene de atanabilir.
                        print "\nGelmesi gereken karakter bilgileri\n-------------------\n "
                        print "Gelmesi gereken karakter=> "+ chr(sayi1)
                        print "ASCII=> ",sayi1
                        ###################################################################################################################################################
                        print "\nEger girdiginiz karakter 'gelmesi gereken karakter bilgileri kısmındaki karakter' ise seri ekrana 'e' degilse 'h' karakterini giriniz.\n"
                        ser.write('\nLutfen cevabiniz evet ise  [e] veya hayir ise  [h] karakterini giriniz: ')
                        karakter2=ser.read() #seri ekrandan bir karakter girisi izlenir.(bir ustteki soru icin)
                        karakter2_int = ord(karakter2)
                        if karakter2_int == 229: #e'nin yanlis gelmis hali--bit sayisi farkliligi(pc:orangepi= 7bit:8bit ise)
                                ser.write('\nSeri haberlesme yaptiginiz cihazla bu cihaz arasinda veri uzunlugu farklidir. Luften kontrol edin!')
                                ser.write('\nProgramdan cikiliyor\n')
                                print "\nSeri haberlesme yaptiginiz cihazda  bu cihaz arasinda veri uzunlugu farklidir. Luften kontrol edin!"
                                print "\nProgramdan cikiliyor\n\n"
                                break
                        elif karakter2_int == 252 : #h'nin yanlis gelmis hali--baud hizi farkindaki. Buraya sadece  pc:orangepi oranı 2:1 oldugunda girersin.
                                print "\nSeri haberlesme yaptiginiz cihazla  bu cihaz arasinda baud hizlari farklidir. Luften kontrol edin!"
                                print "\nProgramdan cikiliyor\n\n"
                                break
                        elif karakter2_int == 104: #h'nin normal durumdaki ASCII karsiligi
                                print"\nBu durumun olusmasinin sebebi\n1)Turkce karakter girmis olabilirsiniz\n2)ASCII kodu 127\'den buyuk bir karakter girmis olabilirsiniz, bu karakterler hata verir.\n"
                                continue
                        elif karakter2_int == 255: #h'nin yanlis gelmis hali --baud hizi farklidir. seri:orangepi oranı 4:1 ve daha buyuk  oldugunda girersin.( 8:1 haric)
                                print "\nSeri haberlesme yaptiginiz cihazda  bu cihaz arasinda baud hizlari farklidir. Luften kontrol edin!"
                                print "\nProgramdan cikiliyor\n\n"
                                break
                        elif karakter2_int == 232: #h'nin yanlis gelmis hali --baud hizi farklidir. seri:orangepi oranı 3:2 oldugunda girersin.
                                print "\nSeri haberlesme yaptiginiz cihazda  bu cihaz arasinda baud hizlari farklidir. Luften kontrol edin!"
                                print "\nProgramdan cikiliyor\n\n"
                                break
                        else : #dongu buraya gelmisse baud hizi oranları yukarıda belirtilen oranlardan  farkli bir  orandadir fakat baud hizlari hala esit degildir.
                                print "\nASCII "  #buraya dongude anliyoruz ki pc'deki baud hizi daha dusuk. Bu yuzden seri ekrandan girdigimiz bir karakter birden fazla olarak algilanir.
                                print "\nilk kisim=> ",karakter_int #ispat icin bu karakterden alinan ilk karakter
                                print "\nikinci kisim=> ",karakter2_int #ispat icin bu karakterleden alinan ikinci  karakter
                                print "\nBINARY"
                                print "\nilk kisim=> ",' '.join(format(x, 'b') for x in bytearray(karakter))
                                print "\nikinci kisim=> ",' '.join(format(x, 'b') for x in bytearray(karakter2))
                                print "\nSeri haberlesme yaptiginiz cihazla  bu cihaz arasinda baud hizlari farklidir. Luften kontrol edin!"
                                print "\nProgramdan cikiliyor\n\n"
                                break


                else:
                        print "Girilen karakter=> " + karakter #alinan karakter ekrana yazdirilir.
                        print"\n"
                        print "Girilen karakter ile yazdiginiz karakter birbirini tutuyorsa   seri ekrana 'e' tutmuyor ise 'h' karakterini girin."
                        ser.write('\n')
                        karakter3 = ser.read() #seri ekrandan bir karakter istenir(bir ustteki soru icin)
                        karakter3_int = ord(karakter3)
                        if karakter3_int == 101: #e'nin normalde durumdaki karsiligi. Parametrelerde bir bozukluk yoksa bu donguyu gecsin diye böyle bir secenek belirtiyoruz ki yeni bir karakter girmemiz icin donguyu basa sarsin.
                                continue
                        if karakter3_int == 127 or  karakter3_int == 104:
                                print "\nASCII "  #buraya dongude anliyoruz ki pc'deki baud hizi daha dusuk. Bu yuzden seri ekrandan girdigimiz bir karakter birden fazla olarak algilanir.
                                print "\nilk kisim=> ", (karakter_int) #ispat icin bu karakterden alinan ilk karakter
                                print "\nikinci kisim=> ", (karakter3_int) #ispat icin bu karakterleden alinan ikinci  karakter
                                print "\nBINARY"
                                print "\nilk kisim=> ",' '.join(format(x, 'b') for x in bytearray(karakter))   #str ile farlı bir veri tipini yazdırırken araya virgul koy
                                print "\nikinci kisim=> ",' '.join(format(x, 'b') for x in bytearray(karakter3))
                                print "\nVeri uzunlugu farkli , lutfen kontrol edin!\n" #pc:orangepi=8:7
                                break
                        elif karakter3_int > 0:
                                print "\nASCII "  #buraya dongude anliyoruz ki pc'deki baud hizi daha dusuk. Bu yuzden seri ekrandan girdigimiz bir karakter birden fazla olarak algilanir.
                                print "\nilk kisim=> ", (karakter_int) #ispat icin bu karakterden alinan ilk karakter
                                print "\nikinci kisim=> ", (karakter3_int) #ispat icin bu karakterleden alinan ikinci  karakter
                                print "\nBINARY"
                                print "\nilk kisim=> ",' '.join(format(x, 'b') for x in bytearray(karakter))   #str ile farlı bir veri tipini yazdırırken araya virgul koy
                                print "\nikinci kisim=> ",' '.join(format(x, 'b') for x in bytearray(karakter3))
                                print "\nSeri haberlesme yaptiginiz cihazla  bu cihaz arasinda baud hizlari farklidir. Luften kontrol edinaa"
                                print "\nProgramdan cikiliyor\n\n"
                                break


        time.sleep(0.1)

