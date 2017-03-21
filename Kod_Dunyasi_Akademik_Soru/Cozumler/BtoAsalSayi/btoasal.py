#! /usr/env/python3
import time as t
import Bolenler

"""
Kullanicidan alinan bir sayinin basamaklari ile yazilabilecek tum
asal sayilarin adedini ekrana yazdiran fonksiyon M() olsun.

__ORNEK:__
	M(127):
		| 2 | 7 | 17 | 71 | 127 | 271 |

		= 6

__CIKTI:__
	100.000'e kadar olan sayilar icinde M() fonksiyonundan en buyuk
	sayiyi donduren sayi kactir?

-----------------------------------------------------------------------


Sayi olarak bakmak yerine string olarak bakmaliyim.

***
ba = t.time()
x = Bolenler().asalSayilar(9999)
k = []


for i in x:
	li = [j for j in str(i)]
	li.sort()
	k.append(li)

foo = 0
for foo in range(9999):
    li2 = [j for j in str(foo)]
	li2.sort()
	temp=x.count(li2)



print(li2)

print(temp)



bi=t.time()

print(bi-ba)
***
"""

asallar = Bolenler.asalSayilar(100000)

for i in asallar

def m(sayi: int) -> None:
    parcaliListe = []
    
    if (len(str(sayi))==1)
    for i in asallar:
        parcalar = [j for j in str(i)]
        parcalar.sort()
        parcaliListe.append(parcalar)
    
     


sure1 = t.time()  # Baslangic zamani

for i in range(99999):
    m(i)
sure2 = t.time() # Bitis zamani

print(sure2-sure1)