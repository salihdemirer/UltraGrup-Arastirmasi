def mapping(sayi1,sayi2):
    eleman = str(sayi1)
    a = eleman[0]+"->"+eleman[1]
    b = eleman[1]+"->"+eleman[2]
    c = eleman[2]+"->"+eleman[3]
    d = eleman[3]+"->"+eleman[0]
    birinci_sözlük = {eleman[0]:eleman[1],eleman[1]:eleman[2],eleman[2]:eleman[3],eleman[3]:eleman[0]}
    print(a+"\n"+b+"\n"+c+"\n"+d+"\n")
    eleman2 = str(sayi2)
    e = eleman2[0]+"->"+eleman2[1]
    f = eleman2[1]+"->"+eleman2[2]
    g = eleman2[2]+"->"+eleman2[3]
    h = eleman2[3]+"->"+eleman2[0]
    ikinci_sözlük = {eleman2[0]:eleman2[1],eleman2[1]:eleman2[2],eleman2[2]:eleman2[3],eleman2[3]:eleman2[0]}
    print(e+"\n"+f+"\n"+g+"\n"+h+"\n")
    print(birinci_sözlük)
    print(ikinci_sözlük)
    #Birinci sözlük ve ikinci sözlük arasındaki eşleşmeleri bulup sonuç yazımından kaldırmam gerekiyor buradaki kodda o işlemler için uğraşacağım.
    if(ikinci_sözlük['1']==birinci_sözlük[ikinci_sözlük['1']]):
    if(ikinci_sözlük['1']==birinci_sözlük[ikinci_sözlük['1']]):
    if(ikinci_sözlük['1']==birinci_sözlük[ikinci_sözlük['1']]):
    if(ikinci_sözlük['1']==birinci_sözlük[ikinci_sözlük['1']]):
    print(birinci_sözlük[ikinci_sözlük['1']]+birinci_sözlük[ikinci_sözlük['2']]+birinci_sözlük[ikinci_sözlük['3']]+birinci_sözlük[ikinci_sözlük['4']])
mapping(1423,1432)
