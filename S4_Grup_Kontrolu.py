#Sadece s4 grubu için hesaplanacak
birim_sozlugu = {'1':'1','2':'2','3':'3','4':'4'}
def sayi_kontrol(sayi):
    bosluk_sayisi = 0
    sayi_ = str(sayi)
    sayi_kumesi = [1,2,3,4]
    #Eğer aynı rakam birden fazla varsa sayıyı hatalı döndürmeliyim !!!!!!
    if(len(str(sayi_))>5):
        print('Verilen sayı S4 grubu için uyumsuz')
        return(0)
    for i in range(0,len(sayi_)):
        if(sayi_[i]==' '):
            bosluk_sayisi = bosluk_sayisi + 1
    if(bosluk_sayisi==0):
        print('Verilen sayı S4 grubu için uyumlu')
        return(0)
    if(bosluk_sayisi==1):
        print('Verilen sayı S4 grubu için uyumlu')
        return(1)
    else:
        print('Verilen sayı S4 grubu için uyumsuz')
        return(2)
def esleme_fonksiyonu(sayi):
    es_sozlugu = {}
    sayi_ = str(sayi)
    #Sayı boşluksuz ve 4 elemanlı ise
    if(sayi_kontrol(sayi)==0 and len(sayi_)==4):
        #sayıda boşluk yoksa ve 4 elemanlı ise
        es_sozlugu = {sayi_[0]:sayi_[1],sayi_[1]:sayi_[2],sayi_[2]:sayi_[3],sayi_[3]:sayi_[0]}
    print(es_sozlugu)
    #Sayı boşluksuz ve 3 elemanlı ise
    if(sayi_kontrol(sayi)==0 and len(sayi_)==3):
        es_sozlugu = {sayi_[0]:sayi_[1],sayi_[1]:sayi_[2],sayi_[2]:sayi_[0]}
        sayi_kumesi = [1,2,3,4]
        eleman_kumesi = []
        #aynı sayıdan iki kere olmaması durumunu önceki fonksiyonda kontrol edeceğim
        for i in range(0,len(sayi_)):
            eleman_kumesi.append(sayi_[i])
        print(eleman_kumesi)
        for i in range(0,4):
            if(str(sayi_kumesi[i]) not in eleman_kumesi):
                es_sozlugu[str(sayi_kumesi[i])]=str(sayi_kumesi[i])
        print(es_sozlugu)
    #Sayı boşluksuz ve iki elemanlı ise
    if(sayi_kontrol(sayi)==0 and len(sayi_)==2):
        es_sozlugu = {sayi_[0]:sayi_[1],sayi_[1]:sayi_[0]}
        sayi_kumesi = [1,2,3,4]
        eleman_kumesi = []
        for i in range(0,len(sayi_)):
            eleman_kumesi.append(sayi_[i])
        print(eleman_kumesi)
        for i in range(0,4):
            if(str(sayi_kumesi[i]) not in eleman_kumesi):
                es_sozlugu[str(sayi_kumesi[i])]=str(sayi_kumesi[i])
        print(es_sozlugu)
    #Sayı boşluksuz ve tek elemanlı ise birim eleman sözlüğünü alacağım
    if(sayi_kontrol(sayi_)==0 and len(sayi_)==1):
        es_sozlugu = birim_sozlugu
        print(es_sozlugu)
    #Sayıda tek boşluk var ve boşluk dahil 5 eleman var ise
    if(sayi_kontrol(sayi_)==1 and len(sayi_)==5):
        es_sozlugu = {sayi_[0]:sayi_[1],sayi_[1]:sayi_[0],sayi_[3]:sayi_[4],sayi_[4]:sayi_[3]}
        print(es_sozlugu)
    #Sayıda tek boşluk var ve boşluk dahil 3 eleman var ise
    if(sayi_kontrol(sayi_)==1 and len(sayi_)==3):
        es_sozlugu = birim_sozlugu
        print(es_sozlugu)
    #Sayıda tek boşluk var ve toplamda 4 eleman oluyorsa durumlar kendi içerisinde ikiye ayrılıyor
    if(sayi_kontrol(sayi_)==1 and len(sayi_)==4):
        
        kume = sayi_.split(' ')
        print(kume)
        #Boşluk solunda tek eleman olduğu durumda Örneğin (1)(32)
        if(len(kume[0])==1):
            es_sozlugu = {sayi_[2]:sayi_[3],sayi_[3]:sayi_[2]}
            sayi_kumesi = [1,2,3,4]
            eleman_kumesi = [ sayi_[2],sayi_[3]]
            for i in range(0,len(sayi_kumesi)):
                if(str(sayi_kumesi[i]) not in eleman_kumesi):
                    es_sozlugu[str(sayi_kumesi[i])]=str(sayi_kumesi[i])
            print(es_sozlugu)
        #Boşluk sağında tek eleman olduğu durumda Örneğin (12)(3)
        if(len(kume[0])==2):
            es_sozlugu={sayi_[0]:sayi_[1],sayi_[1]:sayi_[0]}
            sayi_kumesi = [1,2,3,4]
            eleman_kumesi = [ sayi_[0],sayi_[1]]
            for i in range(0,len(sayi_kumesi)):
                if(str(sayi_kumesi[i]) not in eleman_kumesi):
                    es_sozlugu[str(sayi_kumesi[i])]=str(sayi_kumesi[i])
            print(es_sozlugu)
    return(es_sozlugu)
    
# def mapping(sayi1,sayi2):
#     if(sayi_kontrol(sayi1)==1 and sayi_kontrol(sayi2)==1):
def islem(sayi1,sayi2):
    sonuc = ''
    sozluk1 = esleme_fonksiyonu(sayi1)
    sozluk2 = esleme_fonksiyonu(sayi2)
    print(sozluk1)
    print(sozluk2)
    sozluk3= {'1':sozluk1[sozluk2['1']],'2':sozluk1[sozluk2['2']],'3':sozluk1[sozluk2['3']],'4':sozluk1[sozluk2['4']]}
    #print(sozluk1[sozluk2['1']]+sozluk1[sozluk2['2']]+sozluk1[sozluk2['3']]+sozluk1[sozluk2['4']])
    print(sozluk3)
    #Sonuç olarak eşlenme tamamlandı ama bunun gösterimi ayarlanmalı
    esitlik_sayisi = 0
    for i in range(1,5):
        print(sozluk3[str(i)])
        print(sozluk3[sozluk3[str(i)]])
        if(str(i)== sozluk3[sozluk3[str(i)]]): # Burada bakılmak istenene dikkat
            esitlik_sayisi = esitlik_sayisi + 1
    if(esitlik_sayisi== 1):
        sayi_kumesi=[1,2,3,4]
        for i in range(1,5):
            if(str(i)== sozluk3[sozluk3[str(i)]]):
                sayi_kumesi.remove(int(i))
        print(sayi_kumesi)
        #Algoritmada bir hata var bir işlem bir işlemi tutmuyor
        sonuc = str(sayi_kumesi[0])+sozluk3[str(sayi_kumesi[0])]+sozluk3[sozluk3[str(sayi_kumesi[0])]]
    if(esitlik_sayisi==4):
        sayi_kumesi=[1,2,3,4]
        sayi_kumesi.remove(1)
        sayi_kumesi.remove(int(sozluk3['1']))
        print(sayi_kumesi)
        #Sayı kümesi alıp ilk sayı ve onun götürdüğü sayıyı kümeden çıkarttım böylece elimde kalan iki eşitlik var.
        sonuc = '1'+ str(str(sozluk3['1']))+ " " + str(sayi_kumesi[0]) + str(str(sozluk3[str(sayi_kumesi[0])]))
    return(sonuc)
    #En sonda eşitlik sayısı sayacını tekrar sıfırlamalıyım

print(islem('13 24','34'))
