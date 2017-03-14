# !/usr/bin/python3
import Bolenler

attr = Bolenler.Bolenler()
asalListe=attr.asalSayilar(20) #20ye kadar olan tum asal sayilarin listesi.
frekansSozlugu = dict.fromkeys(asalListe,0)

for i in range(2,21):
    """
    2'den 20'ye kadar olan tum sayilarin asal carpanlari bulunur ve bunlar uygun bicimde
    frekans sozlugune aktarilir.

    Bu sayede frekans sozlugunde hangi sayidan kac adet gerektigi tutulur.
    """
    x=attr.asalCarpanlar(i)
    for j in x:
        y=len(j)
        if (y > frekansSozlugu[j[0]]):
            frekansSozlugu[j[0]]=y

temp  = 1

for i in frekansSozlugu:
    """
    Frekans sozlugundeki veriler ve anahtar sozcukler uygun islemlere sokulur.
    Program sonucu temp degiskeninde tutulur.
    """
    a= i**frekansSozlugu[i]
    temp*=a

print(temp)
