set_1 = {
1 : {"isim":"Ali"   ,"yas":20, "notlar":[85,90,78]},
2 : {"isim":"Ceren" ,"yas":22, "notlar":[75,80,85]},
3 : {"isim":"Hakan" ,"yas":23, "notlar":[82,88,84]},
4 : {"isim":"Mehmet","yas":19, "notlar":[60,65,70]},
5 : {"isim":"Elif"  ,"yas":20, "notlar":[78,85,80]}
}
set_2 = {
1 : {"isim":"Veli" ,"yas":20, "notlar":[88,92,80]},
2 : {"isim":"Fatma","yas":23, "notlar":[70,77,79]},
3 : {"isim":"Murat","yas":18, "notlar":[85,89,91]},
4 : {"isim":"Leyla","yas":21, "notlar":[60,64,66]},
5 : {"isim":"Can"  ,"yas":22, "notlar":[90,93,88]}
}
sets = {1: set_1, 2: set_2}

def fonk1(secim_1):

    secilen_set = sets.get(secim_1)
    for i,j in secilen_set.items():
        print(f"İsim: {j["isim"]} | Yaş: {j["yas"]} | Notlar: {j["notlar"]}")
    print("\n")  

def fonk2(secim_2):
    try:
        check = True
        yas_siniri = input("Yaş değeri giriniz: ")
        if not yas_siniri:
            print("\n----> Bu alan boş bırakılamaz.\n\n")
        elif not yas_siniri.isdigit():
            check = False
        elif int(yas_siniri) < 0:
            check = False

        if not check:
            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
        else:
            yas_siniri = int(yas_siniri)
            secilen_set = sets.get(secim_2)
            print(f"{yas_siniri} yaşından büyük olanlar:")
            bulundu = False 

            for i, j in secilen_set.items():
                if j["yas"] > yas_siniri:
                    bulundu = True
                    print("İsim:", j["isim"], "| Yaş:", j["yas"])
            if not bulundu:
                print(f"{yas_siniri} yaşından büyük öğrenci bulunamamıştır.\n\n")
                    
    except ValueError:
        print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")

def fonk3(secim_3):
    ortalamalar = []
    isimler = []
    secilen_set = sets.get(secim_3)
    for i, j in secilen_set.items():
        notlarin_toplami = sum(j["notlar"])
        not_sayisi = len(j["notlar"])
        ortalama = notlarin_toplami / not_sayisi
        ortalamalar.append(ortalama)
        isimler.append(j["isim"])

    max_ortalama = max(ortalamalar)
    max_index = ortalamalar.index(max_ortalama)
    en_yuksek_ortalama_isim = isimler[max_index]

    min_ortalama = min(ortalamalar)
    min_index = ortalamalar.index(min_ortalama)
    en_dusuk_ortalama_isim = isimler[min_index]

    print("Ortalaması en büyük olan öğrenci:")
    print(f"İsim: {en_yuksek_ortalama_isim}, Ortalama: {max_ortalama:.2f}")
    print("Ortalaması en düşük olan öğrenci:")
    print(f"İsim: {en_dusuk_ortalama_isim}, Ortalama: {min_ortalama:.2f}")
 
def fonk4(secim_4):

    ortalamalar = []
    secilen_set = sets.get(secim_4)
    for i, j in secilen_set.items():
            toplam_not = sum(j["notlar"])
            not_sayisi = len(j["notlar"])
            ortalama = toplam_not / not_sayisi
            ortalamalar.append((j["isim"], ortalama))
            ortalamalar.sort(key=lambda x: x[1], reverse=True)

    print("Büyükten küçüğe ortalama sıralamaları:")
    for i,j in ortalamalar:
        print(f"İsim: {i}, Ortalama: {j:.2f}")

def fonk5(secim_5):
    while True:
        try:
            secilen_set = sets.get(secim_5)
            eklenen_isim = input("Eklemek istediğiniz kişinin ismini girin(Çıkış yapmak için 'Enter'): ").capitalize()
            if not eklenen_isim.isalpha():
                print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                break
            else:
                isimler=[]
                for i,j in secilen_set.items():
                    isimler.append(secilen_set[i]["isim"])
                if eklenen_isim in isimler:
                    print("Bu kişi listede mevcuttur.")
                    break
            eklenen_yas = int(input("Eklemek istediğiniz kişinin yaşını girin(Çıkış yapmak için 'Enter'): "))
            if eklenen_yas < 0:
                print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                break
            eklenen_not = int(input("Eklemek istediğiniz kişiye ait notu girin: "))
            if eklenen_not < 0 or eklenen_not > 100:
                print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                break

            eklenen_notlar = []
            eklenen_notlar.append(eklenen_not)
            yeni_anahtar = max(secilen_set.keys()) + 1
            secilen_set[yeni_anahtar] = {"isim":eklenen_isim,"yas":eklenen_yas,"notlar":eklenen_notlar}
            print("Kişi ekleme işlemleri başarıyla tamamlandı!")
            tercih = input("2. notu girmek ister misiniz? E/H: ").strip().capitalize()
            if tercih == "E":
                    eklenen_not_2 = int(input("2. notu giriniz: "))
                    if eklenen_not_2 < 0 or eklenen_not_2 > 100:
                        print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                        break
                    eklenen_notlar.append(eklenen_not_2)
                    secilen_set[yeni_anahtar] = {"isim":eklenen_isim,"yas":eklenen_yas,"notlar":eklenen_notlar}
                    print("2. not başarıyla eklendi!")
                    tercih_2 = input("3. notu girmek ister misiniz? E/H: ").capitalize()
                    if tercih_2 == "E":
                        eklenen_not_3 = int(input("3. notu giriniz: "))
                        if eklenen_not_3 < 0 or eklenen_not_3 > 100:
                            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                            break
                        eklenen_notlar.append(eklenen_not_3)
                        secilen_set[yeni_anahtar] = {"isim":eklenen_isim,"yas":eklenen_yas,"notlar":eklenen_notlar}
                        print("3. not başarıyla eklendi!")
                        print("Kişi ekleme işlemleri başarıyla tamamlandı!")
                        break
                    elif tercih_2 == "H":
                        print("Kişi ekleme işlemleri başarıyla tamamlandı!")
                        break
            elif tercih == "H":
                    print("Kişi ekleme işlemleri başarıyla tamamlandı!")
                    break
            else:
                    print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                    break
        except ValueError:
            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")

def fonk6(secim_6):
    while True:
        secilen_set = sets.get(secim_6)
        silinecek_isim = input("Setten silmek istediğiniz kişinin ismini girin: ").strip().capitalize()
        if not silinecek_isim.isalpha():
            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
        else:
            isimler = []
            for i,j in secilen_set.items():
                isimler.append(j["isim"])
            if silinecek_isim in isimler:
                secilen_set.pop(i)
                print(f"{silinecek_isim} isimli kişi setten silinmiştir!")
                tercih = input("Çıkış yapmak ister misiniz? E/H: ").strip().capitalize()
                if tercih == "E":
                    print("Çıkış yapıldı.")
                    return 
                elif tercih == "H":
                    break
                else:
                    print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
            else:
                print(f"{silinecek_isim} isimli bir kullanıcı bulunamadı.")
                tercih = input("Çıkış yapmak ister misiniz? E/H: ").strip().capitalize()
                if tercih == "E":
                    print("Çıkış yapıldı.")
                    return
                elif tercih == "H":
                    break
                else:
                    print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                break
                  
def fonk7(secim_7):
    secilen_set = sets.get(secim_7)
    degisecek_kisi = input("Bilgilerini değiştirmek istediğiniz kişinin ismini giriniz: ").strip().capitalize()
    isimler = []
    for i,j in secilen_set.items():
        isimler.append(j["isim"])
    degisecek_index = isimler.index(degisecek_kisi)
    tercih = int(input(f"{degisecek_kisi} kişisine ait hangi bilgileri değiştirmek istersiniz?\n1 - İsim\n2 - Yaş\n3 - Not\nSeçim: "))
    if tercih == 1:
        yeni_isim = input((f"{degisecek_kisi} kişisinin yeni ismini giriniz: ")).strip().capitalize()
        if not yeni_isim:
           print("\n----> Bu alan boş bırakılamaz.\n\n")
        else:
            secilen_set[degisecek_index + 1]["isim"] = yeni_isim
            print(f"{degisecek_kisi} kişisinin ismi, {yeni_isim} olarak değiştirilmiştir.")
    elif tercih == 2:
        yeni_yas = int(input(f"{degisecek_kisi} kişisinin yeni yaşını giriniz: "))
        if not yeni_yas:
            print("\n----> Bu alan boş bırakılamaz.\n\n")
        else:
            secilen_set[degisecek_index + 1]["yas"] = yeni_yas
            print(f"{degisecek_kisi} kişisinin yaşı, {yeni_yas} olarak değiştirilmiştir.")
    elif tercih == 3:
        print(f"{degisecek_kisi} kişisinin notları:")
        for i in range(len(secilen_set[1]["notlar"])):
            print(f"{i+1}. Not: {secilen_set[degisecek_index + 1]["notlar"][i]}")
        not_secimi = int(input(f"{degisecek_kisi} kişisinin kaçıncı notunu değiştirmek istersiniz?: "))
        if not not_secimi:
            print("\n----> Bu alan boş bırakılamaz.\n\n")
        else:
            not_yeni = int(input(f"{degisecek_kisi} kişisinin {not_secimi}. notunun yeni değerini giriniz: "))
            if not not_yeni:
                print("\n----> Bu alan boş bırakılamaz.\n\n")
            else:
                secilen_set[degisecek_index + 1]["notlar"][not_secimi - 1] = not_yeni
                print(f"{degisecek_kisi} kişisinin {not_secimi}. notu {not_yeni} olarak değiştirildi.")

def fonk8(secim_8):
    secilen_set = sets.get(secim_8)
    not_eklenecek_kisi = input("Not eklemek istediğiniz öğrencinin ismini yazınız: ").strip().capitalize()
    isimler = []
    for i,j in secilen_set.items():
        isimler.append(j["isim"])
    eklenecek_index = isimler.index(not_eklenecek_kisi)
    yeni_not = int(input(f"{not_eklenecek_kisi} isimli öğrencinin hali hazırda {len(secilen_set[eklenecek_index+1]["notlar"])} notu var, {len(secilen_set[eklenecek_index+1]["notlar"]) + 1}. notu giriniz: "))
    if yeni_not >100:
       print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
    else:
        secilen_set[eklenecek_index+1]["notlar"].append(yeni_not)
        print(f"{not_eklenecek_kisi} isimli öğrencinin {(len(secilen_set[eklenecek_index+1]["notlar"]))}. notu {yeni_not} olarak eklenmiştir.")
    
def fonk9(secim_9):
    secilen_set = sets.get(secim_9)
    notListesi = []
    for i, j in secilen_set.items():
        notListesi.extend(j["notlar"])
    notListesi.sort()
    if len(notListesi) % 2 == 0:
        medyan = (notListesi[(len(notListesi)//2) - 1] + notListesi[(len(notListesi)//2)]) / 2
        print(f"{secim_9}. setteki öğrencilerin notlarından oluşturulmuş medyan değeri: {medyan}")
    else:
        medyan = notListesi[(((len(notListesi))+1)//2) - 1]
        print(f"{secim_9}. setteki öğrencilerin notlarından oluşturulmuş medyan değeri: {medyan}")
    
def fonk10(secim_10):
    secilen_set = sets.get(secim_10)
    notListesi = []
    for i, j in secilen_set.items():
        notListesi.extend(j["notlar"])
    notListesi.sort()
    for i in notListesi:
        notlarin_toplami = sum(notListesi)
        not_sayisi = len(notListesi)
        ortalama = notlarin_toplami / not_sayisi
    standartSapmaPay = []
    for i in range(len(notListesi)):
        standartSapmaPay.append((notListesi[i] - ortalama)**2)
    standartSapmaPayToplami = sum(standartSapmaPay)
    standartSapma = ((standartSapmaPayToplami / (len(notListesi)-1))**0.5)
    
    print(f"{secim_10}. setteki öğrencilerin notlarından oluşturulan standart sapma değeri: {standartSapma}")
    
def fonk11(secim_11):
    try:
        print("Kıyaslama ekranına hoş geldiniz!\n2 adet öğrenci seçmeniz gerekmektedir.")
        secilen_set = sets.get(secim_11)
        isimler = []
        for i,j in secilen_set.items():
            isimler.append(j["isim"])
        print(f"{secim_11}. setteki kişiler:\n---------")
        for i in range(len(secilen_set.items())):
            print(f"{i+1}. {secilen_set[i+1]["isim"]}")
        kiyas1 = input("\n1. Öğrencinin ismi: ").strip().capitalize()
        if kiyas1 not in isimler:
            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
        else:
            kiyas2 = input("2. Öğrencinin ismi: ").strip().capitalize()
            if kiyas2 not in isimler:
                print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
            else:
                hangisi = int(input("Öğrencileri hangi özellik bakımından kıyaslamak istersiniz?\n1 - Yaş\n2 - Notlar\nSeçim(1/2): "))
                if hangisi == 1:
                    isimler = []
                    for i in range(len(secilen_set.items())):
                        isimler.append(secilen_set[i+1]["isim"])
                    kiyas1index = isimler.index(kiyas1)
                    kiyas2index = isimler.index(kiyas2)
                    print(f"--> {kiyas1} isimli öğrencinin yaşı: {secilen_set[kiyas1index+1]["yas"]}")
                    print(f"--> {kiyas2} isimli öğrencinin yaşı: {secilen_set[kiyas2index+1]["yas"]}")
                    if secilen_set[kiyas1index+1]["yas"] > secilen_set[kiyas2index+1]["yas"]:
                        print(f"----> {kiyas1}, {kiyas2} öğrencisinden daha yaşlıdır.\n")
                    elif secilen_set[kiyas1index+1]["yas"] < secilen_set[kiyas2index+1]["yas"]:
                        print(f"----> {kiyas2}, {kiyas1} öğrencisinden daha yaşlıdır.\n")
                    else:
                        print(f"----> {kiyas1} ve {kiyas2} öğrencilerinin yaşları eşittir.\n")

                elif hangisi == 2:
                    isimler = []
                    for i in range(len(secilen_set.items())):
                        isimler.append(secilen_set[i+1]["isim"])
                    kiyas1index = isimler.index(kiyas1)
                    kiyas2index = isimler.index(kiyas2)
                    for i, j in secilen_set.items():
                        notlarin_toplami = sum(secilen_set[kiyas1index+1]["notlar"])
                        not_sayisi = len(j["notlar"])
                        ortalama1 = notlarin_toplami / not_sayisi
                        
                        notlarin_toplami_2 = sum(secilen_set[kiyas2index+1]["notlar"])
                        not_sayisi_2 = len(j["notlar"])
                        ortalama2 = notlarin_toplami_2 / not_sayisi_2

                    print(f"--> {kiyas1} isimli öğrencinin ortalama notu: {ortalama1:.2f}")
                    print(f"--> {kiyas2} isimli öğrencinin ortalama notu: {ortalama2:.2f}")
                    if ortalama1 > ortalama2:
                        print(f"----> {kiyas1}, {kiyas2} öğrencisine göre daha başarılıdır.\n")
                    elif ortalama2 > ortalama1:
                        print(f"----> {kiyas2}, {kiyas1} öğrencisine göre daha başarılıdır.\n")
                    else:
                        print(f"----> {kiyas1} ve {kiyas2} öğrencilerinin başarıları eşittir.\n")
                else:
                    print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
    except ValueError:
        print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")


def fonk12(secim_12):
    secilen_set = sets.get(secim_12)
    grup_75_100 = []
    grup_50_75 = []
    grup_0_50 = []
    for i, j in secilen_set.items():
        notlarin_toplami = sum(j["notlar"])
        not_sayisi = len(j["notlar"])
        ortalama = notlarin_toplami / not_sayisi

        if 75 <= ortalama <= 100:
            grup_75_100.append(j["isim"])
        if 50 <= ortalama < 75:
            grup_50_75.append(j["isim"])
        if 0 <= ortalama < 50:
            grup_0_50.append(j["isim"])

    print(f"Başarılı öğrenciler      [75 - 100]:", ", ".join(grup_75_100) if grup_75_100 else "Yok")
    print(f"Orta başarılı öğrenciler [50 - 75) :", ", ".join(grup_50_75) if grup_50_75 else "Yok")
    print(f"Başarısız öğrenciler     [0 - 50)  :", ", ".join(grup_0_50) if grup_0_50 else "Yok")

def fonk13(secim_13):
    secilen_set = sets.get(secim_13)
    setin_yaslari = []
    yaslarin_isimleri = []
    for i,j in secilen_set.items():
        setin_yaslari.append(j["yas"])
        yaslarin_isimleri.append(j["isim"])

    yasli = max(setin_yaslari)
    yaslinin_index = setin_yaslari.index(yasli)
    yaslinin_ismi = yaslarin_isimleri[yaslinin_index]

    genc = min(setin_yaslari)
    gencin_index = setin_yaslari.index(genc)
    gencin_ismi = yaslarin_isimleri[gencin_index]

    print(f"{secim_13}. setin\n---> En yaşlı öğrencisi: {yaslinin_ismi}, {yasli}")
    print(f"---> En genç öğrencisi: {gencin_ismi}, {genc}")

def fonk14(secim_14):
        secilen_set = sets.get(secim_14)
        tum_notlar = []
        not_sayisi = 0
        for i,j in secilen_set.items():
            tum_notlar.append(sum(j["notlar"]))
            not_sayisi += len(j["notlar"])
        
        tum_notlar = sum(tum_notlar)
        ortalama = tum_notlar / not_sayisi
        print(f"{secim_14}. setteki tüm öğrencilerin notlarının toplamı: {tum_notlar}")
        print(f"Notların ortalaması: {ortalama:.2f}")

def anaFonksiyon():
    print("Öğrenci paneline hoş geldiniz. Seçeceğiniz öğrenci grubu üzerinden çeşitli işlemler yapabileceksiniz.")
    while True: 
        try:
            print("Öğrenci grupları:")
            isimler_set1 = []
            for i,j in set_1.items():
                isimler_set1.append(j["isim"])
            isimler_set2 = []
            for i,j in set_2.items():
                isimler_set2.append(j["isim"])
            print(f"----> 1. Grup öğrencileri: {isimler_set1}\n----> 2. Grup öğrencileri: {isimler_set2}")

            secim = int(input("Seçim: "))
            if secim not in (1, 2):
                print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")
                continue 
            else:
                break
            
        except ValueError:
            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")

    while True:
        try:
            print("*"*54)
            print("Yapmak istediğiniz işlemi seçiniz")
            print("1  - Öğrenci bilgilerini yazdır")
            print("2  - Belirli bir yaşın üzerindeki öğrencileri yazdır")
            print("3  - En yüksek ve en düşük ortalamaya sahip öğrencileri yazdır")
            print("4  - Her öğrencinin ortalama notunu yazdır, büyükten küçüğe sırala")
            print("5  - Yeni bir öğrenci ekle")
            print("6  - Öğrenci sil")
            print("7  - Öğrencinin bilgilerini değiştir")
            print("8  - Öğrenciye yeni not ekle")
            print("9  - Bütün notların medyanını yazdır")
            print("10 - Bütün notların standart sapmasını yazdır")
            print("11 - İki öğrenciyi kıyasla")
            print("12 - Öğrencileri notlarına göre kategorize et")
            print("13 - En genç ve en yaşlı öğrenciyi yazdır")
            print("14 - Bütün notların toplamını ve ortalamasını yazdır")
            print("15 - Öğrenci grubu seçimini tekrar yap")
            print("16 - Programı sonlandır")
            secim_gorev = int(input("Seçiminizi yapınız: "))
            print("*"*54)

            if secim_gorev == 1:
                fonk1(secim)
            elif secim_gorev == 2:
                fonk2(secim)
            elif secim_gorev == 3:
                fonk3(secim)
            elif secim_gorev == 4:
                fonk4(secim)
            elif secim_gorev == 5:
                fonk5(secim)    
            elif secim_gorev == 6:
                fonk6(secim)
            elif secim_gorev == 7:
                fonk7(secim)
            elif secim_gorev == 8:
                fonk8(secim)
            elif secim_gorev == 9:
                fonk9(secim)
            elif secim_gorev == 10:
                fonk10(secim)
            elif secim_gorev == 11:
                fonk11(secim)
            elif secim_gorev == 12:
                fonk12(secim)
            elif secim_gorev == 13:
                fonk13(secim)
            elif secim_gorev == 14:
                fonk14(secim)
            elif secim_gorev == 15:
                print(anaFonksiyon())
            elif secim_gorev == 16:
                print("Program başarıyla sonlandırıldı!")
                exit()
            elif secim_gorev not in (1,16):
                print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")    
        except ValueError:
            print("\n----> Hatalı değer girdiniz, lütfen tekrar deneyiniz.\n\n")

# ---------------
anaFonksiyon() #-
#----------------