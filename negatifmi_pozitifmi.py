#!/usr/bin/env python
# -*- coding:utf-8 -*-

negatifmi_pozitifmi_ico = """
#################################################################
#     PYTHON - Negatif mi ? Pozitif mi ? - GH0ST S0FTWARE       #
################################################################# 
#                           CONTACT                             #
#################################################################
#                  DEVELOPER : İSMAİL TAŞDELEN                  #                       
#               GMAIL : pentestdatabase@gmail.com               #
#       Linkedin : https://www.linkedin.com/in/ismailtasdelen   #
#                 Whatsapp : + 90 534 295 94 31                 #
#################################################################
"""

print negatifmi_pozitifmi_ico

star = "#################################################################"

print star

sayi = float(input("Bir sayı giriniz : "))

print star

negatif_mesaj_ico = "Girdiğiniz sayı negatifdir."
pozitif_mesaj_ico = "Girdiğiniz sayı pozitifdir."
notr_mesaj_ico = "Girdiğiniz sayı nötrdür."

if sayi < 0:
	print "Sonuç : " + negatif_mesaj_ico
	print star
	
elif sayi == 0:
	print "Sonuç : " + notr_mesaj_ico
	print star
else:
	print "Sonuç : " + pozitif_mesaj_ico
	print
