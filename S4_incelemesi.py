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
print(indis_kumeler_kumesi)
print("\n")
print(kumeler_kumesi)
print(len(kumeler_kumesi))
es_elemanlar = []
print("İndis kümeler kümesi \n")
print(indis_kumeler_kumesi)
# for i in range(0,len(kumeler_kumesi)):
#     for j in range(0,len(kumeler_kumesi)):
#         for k in range(0,len(kumeler_kumesi[i])):
#             kume1 = kumeler_kumesi[i]
#             kume2 = kumeler_kumesi[j]
#             if(kume1[k] in kume2):
#                 sayac = sayac + 1
#         if(sayac == len(kume1)):
#             kumeler_kumesi.remove(kumeler_kumesi[j])
print('Kaçıncı işlemde olduğunun tespiti \n')
#print(kumeler_kumesi.index(['1321', '14', '23', '1231', '134', '142', '123', '243']))
kumeler_kumesi = sorted(kumeler_kumesi)
for i in kumeler_kumesi:
    sayac = 0
    for j in kumeler_kumesi:
        for k in range(0,len(i)):
            if(i[k] in j):
                sayac = sayac + 1
        if(sayac == len(i)):
            kumeler_kumesi.remove(j)
    sayac = 0
print('Eşkümeler yazdırılıyor')
print(kumeler_kumesi)
print(len(kumeler_kumesi))
print(kumeler_kumesi.count(['132', '143', '234', '124', '13', '1432', '1234', '24']))
print(kumeler_kumesi.count(['1423', '1324', '12', '34', '14 23', '13 24', '', '12 34']))