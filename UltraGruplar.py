#İlk önce girilen parametre kontrol edilecek. Parantez sayısı gerekiyor
kritik_sozluk = {'1':'1','2':'2','3':'3','4':'4'}
def parantez_kontrol(string):
    karakter_sayisi = len(string)
    koleksiyon = []
    koleksiyon_= ''
    for i in range(0,karakter_sayisi):
        if(string[i]=='('):
            koleksiyon.append(string[i])
        if(string[i]==')'):
            koleksiyon.append(string[i])
    print(koleksiyon)
    for i in koleksiyon:
        koleksiyon_ += i
    print(koleksiyon_)
    if(koleksiyon_=="()"):
        print('Girilen veriler işlem için uygun')
        return(1)
    if(koleksiyon_=="()()"):
        return(2)
    else:
        print('Girilen veriler işlem için hatalı!')
        return(0)
def mapping(sayi1,sayi2):
    #Kontrol işlemleri düzenlenmeli parantez bilgileri alınıp parantez içerisindeki sayılar alınmalı sonra işlem tanımlanabilir.
    if((parantez_kontrol(sayi1)==1 and parantez_kontrol(sayi2)==1 )or (parantez_kontrol(sayi1)==2 and parantez_kontrol(sayi2)==2) or  (parantez_kontrol(sayi1)==1 and parantez_kontrol(sayi2)==2) or  (parantez_kontrol(sayi1)==2 and parantez_kontrol(sayi2)==1) ):
        if(parantez_kontrol(sayi1)==1):

            print(sayi1)
        print('İşlemler uygun')
    else:
        print("Girilen veriler işlem için uygun değil")
mapping('(1234)','(12312)')