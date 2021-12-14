from S4_Grup_Kontrolu import islem
s4 = ['1','12','13','14','23','24','34','123','124','134','142','143','132','234','243','12 34','13 24','14 23','1234','1243','1342','1324','1432','1423']
h = ['1','12 34','13 24','14 23','12','34','1324','1423']
kume = []
kumeler_kumesi = []
indis_kumesi = []
indis_kumeler_kumesi = []
for i in s4:
    for j in h:
        indis_kumesi = []
        kume.append(islem(j,i))
        indis_kumesi.append(j)
        indis_kumesi.append(i)
        indis_kumeler_kumesi.append(indis_kumesi)
    kumeler_kumesi.append(kume)
    kume = []
es_elemanlar = []
for k in kumeler_kumesi:
    sorted(k)
eskumeler = []
eskumeler.append(kumeler_kumesi[0])
kume1 = kumeler_kumesi[0]
kumeler_kumesi.remove(kumeler_kumesi[0])
for i in kumeler_kumesi:
    sayac = 0
    for j in range(0,len(kumeler_kumesi[0])):
            if(kume1[j] in i):
                sayac = sayac + 1
    if(sayac == len(kume1)):
        if(i in kumeler_kumesi):
            kumeler_kumesi.remove(i)
eskumeler.append(kumeler_kumesi[0])
kume2 = eskumeler[1]
for i in kumeler_kumesi:
    sayac = 0
    for j in range(0,len(kumeler_kumesi[0])):
        if(kume2[j] in i):
            sayac = sayac + 1
    if(sayac == len(kume2)):
        if(i in kumeler_kumesi):
            kumeler_kumesi.remove(i)
eskumeler.append(kumeler_kumesi[0])
print("H\G = "+str(eskumeler))

m_kumesi = []
for i in eskumeler[0]:
    kume = []
    for j in eskumeler[1]:
        for k in eskumeler[2]:
            kume.append(i)
            kume.append(j)
            kume.append(k)
            m_kumesi.append(kume)
            kume = []
kume = []
for i in m_kumesi:
        if('1' in i):
            #m_kumesi.remove(i)
            kume.append(i)
print('-------------')
print(str(len(kume))+'Adet seçilebilecek M kümesi kombinasyonu var')
for i in range(0,len(kume)):
    print('M'+str(i+1)+'='+str(kume[i]))

def alpha_table(kume,sonuc_kumesi):
    print(str(kume)+' M kümesi için\n')
    print('Alfa'+' | '+str(kume[0])+'  | '+str(kume[1])+'  | '+str(kume[2]))
    print('------------------------')
    print(' '+str(kume[0])+'  |  '+str(sonuc_kumesi[0])+'  | '+str(sonuc_kumesi[1])+'  | '+str(sonuc_kumesi[2]))
    print('------------------------')
    print(' '+(kume[1])+'  |  '+str(sonuc_kumesi[3])+'  | '+str(sonuc_kumesi[4])+'  | '+str(sonuc_kumesi[5]))
    print('------------------------')
    print(' '+(kume[2])+'  |  '+str(sonuc_kumesi[6])+' | '+str(sonuc_kumesi[7])+' | '+str(sonuc_kumesi[8]))
    print('\n')
    print('\n')
def beta_table(kume,h,sonuc_kumesi):
    print(str(kume)+' eşkümesi ve H\G='+str(h)+' için')
    print('Beta'+' | '+str(h[0])+'  | '+str(h[1])+'  | '+str(h[2])+'  | '+str(h[3])+'  | '+str(h[4])+'  | '+str(h[5])+'  | '+str(h[6])+'  | '+str(h[7]))
    print('------------------------------------------------------------------------')
    print(kume[0]+' | '+str(sonuc_kumesi[0])+'  | '+str(sonuc_kumesi[1])+'  | '+str(sonuc_kumesi[2])+'  | '+str(sonuc_kumesi[3])+'  | '+str(sonuc_kumesi[4])+'  | '+str(sonuc_kumesi[5])+'  | '+str(sonuc_kumesi[6])+'  | '+str(sonuc_kumesi[7]))
    print('------------------------------------------------------------------------')
    print(kume[1]+' | '+str(sonuc_kumesi[8])+'  | '+str(sonuc_kumesi[9])+'  | '+str(sonuc_kumesi[10])+'  | '+str(sonuc_kumesi[11])+'  | '+str(sonuc_kumesi[12])+'  | '+str(sonuc_kumesi[13])+'  | '+str(sonuc_kumesi[14])+'  | '+str(sonuc_kumesi[15]))
    print('------------------------------------------------------------------------')
    print(kume[2]+' | '+str(sonuc_kumesi[16])+'  | '+str(sonuc_kumesi[17])+'  | '+str(sonuc_kumesi[18])+'  | '+str(sonuc_kumesi[19])+'  | '+str(sonuc_kumesi[20])+'  | '+str(sonuc_kumesi[21])+'  | '+str(sonuc_kumesi[22])+'  | '+str(sonuc_kumesi[23]))
    print('\n')

def alpha(kume,eskumeler):
    kontrol = 0
    sonuc_kumesi = []
    for i in kume:
        for j in kume:
            for k in eskumeler: #Eşkümeler kümesinde 3 elemandan ilk elemana göre kontrol etmek istediğimiz için
                if(islem(k,islem(i,j)) in kume):
                    sonuc_kumesi.append(islem(k,islem(i,j)))
    
    alpha_table(kume,sonuc_kumesi)
   
               
     
# Kumeyi gönderirken for içerisinde göndermem gerekiyor.

k_ = set()
def beta(kume,h):
    sonuc_kumesi_ = []
    for i in kume:
        for j in h:
            for m in h: #Burda değişken h da olabilir aynı değişken gönderiliyor
                if(islem(m,islem(i,j)) in kume):
                    sonuc_kumesi_.append(str(islem(m,islem(i,j))))
    beta_table(kume,h,sonuc_kumesi_)

# for i in kume:
#     for j in eskumeler:
#         alpha(i,j)


h_ = [['1','12 34','13 24','14 23','12','34','1324','1423'],['13','24','124','143','132','234','1234','1432'],['14','23','123','134','142','243','1243','1342']]
for i in h_:
    for i in kume:
        beta(i,h)

#alpha(kume[0],eskumeler[0])
#beta(kume[0],eskumeler[0])