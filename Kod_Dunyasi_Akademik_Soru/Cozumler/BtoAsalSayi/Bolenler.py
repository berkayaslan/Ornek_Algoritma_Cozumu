#! /usr/env/bin python3

def farkliAsalCarpanlar(sayi): #FIXME: Daha hizli yapilmasi denenebilir.
	"""
	Alinan sayinin birbirinden farkli tum asal carpanlarini geri donduren fonksiyon.
	Kume dondurmesi yerine yeniden kullanilabilirlik acisindan liste donduruyor.

	ARGS:
		sayi: Asal carpanlarinin bulunmasi istenen sayi

	RETURNS:
		list(): Asal carpanlarin listesi.
	"""
	return tuple([x for x in self.asalSayilar(sayi) if (sayi%x==0)])

def asalSayilar(limit):
	"""
	Verilen limit degerine kadarki tum asal sayilari bulan fonksiyon. Buldugu asal
	sayilari hafizasindaki listeye ekler. Baslangicta listede 2 sayisi vardir. Algoritma
	geregi listede ilk eleman bulunmalidir.

	ARGS:
		limit: Asal sayilarin bulunacagi ust limit

	RETURNS:
		asalSayilarListe = Asal sayilarin bulundugu liste
	"""
	asalSayilarListe = [2]
	foo = 3

	while (foo <= limit):
		bayrak = 1

		for bar in asalSayilarListe: #Dongu sayisini kendinden onceki asal sayilara boler.
			if (bar > (foo**0.5)): #Kendinden onceki sayilara degil kokunden oncekilere
				break

			if (foo%bar == 0):
				bayrak = 0
				break

		if (bayrak == 1): asalSayilarListe.append(foo)
		foo += 2

	return tuple(asalSayilarListe)

def asalCarpanlar(sayi): #IDEA: Tum carpanlarinin eklenmesi yerine carpanlarinin
# yanina ust ifadesi eklenebilir.
	"""
	Alinan sayinin asal carpanlarinin bulundugu ve donduruldugu fonksiyon. Tum asal
	sayi bolenleri bir demet halinde verilir.

	Verilen demet duzensiz ve 2 boyutlu bir demettir. Ornegin 12 sayisi icin verilen
	sonuc:

		self.asalCarpanlar(12) = ( ( 2, 2 ), ( 3 ) )

	NOT: Demetler sonradan degistirilemez. Ama yeniden tanimlanabilir.

	ARGS:
		sayi: Asal carpanlarinin bulunmasi istenen sayi.

	RETURNS:
		tuple(tuple()....) : Asal carpanlar demeti
	"""
	carpanListesi=[]
	asalCarpanListesi=self.farkliAsalCarpanlar(sayi)
	sayi=sayi

	for i in asalCarpanListesi:
		carpan=[]
		while (sayi%i == 0):
			carpan.append(i)
			sayi = sayi/i
		carpanListesi.append(tuple(carpan))

	return tuple(carpanListesi)

def pozitifBolenToplami(sayi):
	"""
	Verilen sayinin pozitif bolenlerinin toplamini bulan fonksiyon.
	Matematiksel bir formul kullanir.

	ARGS:
		sayi: islemlerin yapilmasinin istendigi sayi

	RETURNS:
		temo: sayi'nin tum pozitif bolenlerinin toplami.
	"""
	alttakiler= self.farkliAsalCarpanlar(sayi)
	usttekiler = list(map(lambda x: len(x), self.asalCarpanlar(sayi)))

	j = 0
	temp = 1
	for i in usttekiler:
		x=(alttakiler[j]**(i+1)-1)/(alttakiler[j]-1)
		temp*=x
		j+=1

	return temp
		
