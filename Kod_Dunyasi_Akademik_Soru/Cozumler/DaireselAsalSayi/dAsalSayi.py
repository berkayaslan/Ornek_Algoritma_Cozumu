import time

def main():
    sayac = 0
    for i in range(2, 1001):
        if asalMi(i):  # Sayinin kendisi asal degilse diger islemleri yapmaya gerek yok.
            temp = i
            flag = 1
            
            for j in range(len(str(i))):  # Basamak sayisi kadar sayiCevir() fonksiyonu cagrilir.
                temp = sayicevir(temp)
                if not asalMi(temp):
                    flag=0
                    break
            
            if flag == True:
                sayac += 1
                # print(i)  # [OPTIONAL] Sayilari yazdirmak istersen.
    
    print(sayac)

    
def sayicevir(sayi: int) -> int:
    """
    Sayilari bir basamak sola kaydiran fonksiyon.
    (Soruda istenmis)
    """
    sayi = str(sayi)
    dList = []
    
    foo = 1
    
    while foo<len(sayi):
        dList.append(sayi[foo])
        foo += 1
    
    dList.append(sayi[0])
    
    return int("".join(dList))


def asalMi(sayi: int) -> bool:
    """
    Asal sayi kontrolunu saglayan fonksiyon.
    """
    bayrak = True
    kok = sayi**0.5  # Sayiya kadar olan sayilari denetlemez. Kokune kadar olanlari denetler.
    sayac = 2
    
    while sayac <= kok:
        if sayi%sayac == 0:
            bayrak = False
            break
        sayac += 1
    
    return bayrak



if __name__ == "__main__":
    baslangicSaati = time.time()  # OPTIONAL: Sure icin
    
    main()
    
    bitisSaati = time.time()  # OPTIONAL Sure icin
    
    print("\n\n%f surede tamamlandi!" % (bitisSaati - baslangicSaati))
