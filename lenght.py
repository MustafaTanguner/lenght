#!/usr/bin/python3
import os
from termcolor import colored
import time
import sys
print(colored("""

---------------------------------



      Özel Uzunluk Sayacı 



       Author:@villwocki




---------------------------------



	""",'red'))
ac = open(input(colored("Dosya yolunu giriniz:",'cyan')))

test = open("sonuc.txt",'w')
x = int(input(colored("Harf uzunluğunu giriniz::",'red')))
try:
	for i in ac:
		if len(i) == int(x):
			print("Buldu!!::",i)
			test.write(i)

except:
	print(bool(x))

test.close()
time.sleep(1)
print(colored("\nSonuc.txt kayit edildi...",'green'))
