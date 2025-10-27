ism = "BOBUR"
uy_manzili = "TOSHKENT"

print(ism.capitalize())
print(uy_manzili.lower())
print(uy_manzili.upper())
print(ism.title())

hayvonlar = ['it', 'mushuk', 'quyon', 'to\'ti', 'chumoli'] 
oila = ['ota', 'ona', 'aka', 'uka', 'opa', 'singil']
mashinalar = ['nexia', 'gentra', 'malibu', 'bmw', 'audi']


hayvonlar = ['it', 'mushuk', 'quyon', 'to\'ti', 'chumoli']
print(hayvonlar)
qiymat = hayvonlar[3]
print(qiymat)
print(hayvonlar[0])   
print(hayvonlar[1])
print(hayvonlar[-5])
mashinalar = ['nexia', 'gentra', 'malibu', 'bmw', 'audi']

royxat = [1, 2, 3, 4, 5]
print(royxat)
print(royxat[0])
print(royxat[1]) 
print(royxat[-5])

mevalar = ['olma', 'anor', 'banan', 'shaftoli', 'o\'rik']
print(mevalar.index('banan'))
print(mevalar.index('o\'rik'))
print(mevalar.index('olma'))
print(mevalar.index('anor'))  
print(mevalar.index('shaftoli'))
print(mevalar[2].title())
print(mevalar[3].upper())
print(mevalar[0].capitalize())
print(mevalar[1].lower())
print(mevalar[4].title())
print(mevalar[-1].upper())
print(mevalar[-2].lower())
print(mevalar[-3].capitalize())
print(mevalar[-4].title())
print(mevalar[-5].upper())


# append(), insert(), remove() bilan ro‘yxatni boshqarish

it_oquvchilar = []
gurux = it_oquvchilar.append("Komolbek")
gurux = it_oquvchilar.append("Umid")

print(it_oquvchilar)


dostlar = []
dostlar.append("Ali")
dostlar.append("Vali")
dostlar.append("Sardor")

print("Dastlabki ro'yxat:", dostlar)

dostlar.insert(1, "Dilshod")  # 1-pozitsiyaga joylashtiradi
print("Insertdan keyin:", dostlar)

dostlar.remove("Ali")  # Ali ni o'chiramiz
print("Removdan keyin:", dostlar)


# pop metodi

mevalar = ['olma', 'anor', 'banan', 'o\'rik']
print("Barcha mevalar:", mevalar)

oxirgisi = mevalar.pop()  # oxirgisini o'chiradi
print("O'chirilgan:", oxirgisi)
print("Qolganlar:", mevalar)

birinchisi = mevalar.pop(0)  # 0-indeksdagisini o'chiradi
print("Birinchisi:", birinchisi)
print("Qolganlar:", mevalar)



# sort() va reverse() bilan tartiblash

mashinalar = ['bmw', 'audi', 'nexia', 'malibu', 'gentra']
print("Boshlang'ich:", mashinalar)

mashinalar.sort()  # alifbo tartibida
print("Tartiblangan:", mashinalar)

mashinalar.reverse()  # teskari tartibda
print("Teskari:", mashinalar)



# len() va for bilan aylanma (loop)

shaharlar = ['Toshkent', 'Samarqand', 'Buxoro', 'Namangan']

print("Shaharlar soni:", len(shaharlar))
for shahar in shaharlar:
    print("Men", shahar, "shahrini yaxshi ko'raman!")

#  kitoblar ro'yxatini yaratish va unga qiymatlar qo'shish

kitoblar = []

# append() yordamida element qo'shamiz (ro'yxat oxiriga qo'shadi)
kitoblar.append("Python asoslari")
kitoblar.append("Sun’iy intellekt")
kitoblar.append("Dasturlash sirlari")

print("Kitoblar ro'yxati:", kitoblar)











