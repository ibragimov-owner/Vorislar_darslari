#          masala 1
# for1: k va n butun sonlar berilgan (n>0) . k sonini n marta chiqaruvchi programma tuzilsin
# print("k sonini n marta chiqaruvchi programma")
# k =  int(input("k sonini kiriting:"))
# n = int(input("n sonini kiriting: (n>0):"))

# for son in range(1, n+1):
#    print(f"{son} - sikl:" ,{k})



#          masala 2
# For2. a va b butun sonlari berilgan (a < b). a va b sonlari orasidagi barcha butun sonlami (a va b ni ham) chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi programma tuzilsin. (a va b xam chiqarilsin).
# a = int(input("a ni kiriting (a < b): "))
# b = int(input("b ni kiriting: "))


# print("a dan b gacha bo'lgan sonlar:")
# sonlar = list(range(a, b + 1))
# for son in sonlar:
#     print(son)

# print("chiqarilgan sonlar soni:",len(sonlar))



#          masala 3
# For3. a va b butun sonlari berilgan (a < b). a va b sonlari orasidagi barcha butun sonlarni (a va b dan tashqari) kamayish tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi progma tuzilsin.
# a = int(input("a sonini kiriting (a<b): "))
# b = int(input("b sonini kiriting (a<b): "))
# son = 0
# for i in range(b-1, a, -1):
#       print(i)
#       son += 1
# print(f"Chiqarilgan sonlar soni: {son}")



#       masala 4
# for4: Bir kg konfetning narxi berilgan (haqiqiy son). 1, 2, ... , 10 kg konfetni narxini chiqaruvchi programma tuzilsin.
# narx = float(input("Bir kg konfetning narxini kiriting: "))

# for kg in range(1, 11):
#     summa = kg * narx
#     print(f"{kg} kg konfetning narxi: {summa} so'm")



#         masala 5
# for5: Bir kg konfetning narxi berilgan (haqiqiy son). 0.1, 0.2, ... , 1 kg konfetni narxini chiqaruvchi programma tuzilsin.
# narx = float(input("Bir kg konfetning narxini kiriting: "))
# for kg in range(1, 11):
#     kg_kg = kg / 10
#     summa = kg_kg * narx
#     print(f"{kg_kg} kg konfetning narxi: {summa} so'm")



#             masala 6
# for6: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha butun sonlarning kvadratlarini chiqaruvchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# for son in range(1, n + 1):
#     kvadrat = son ** 2
#     print(f"{son} ning kvadrati: {kvadrat}")



#             masala 7
# for7: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha butun sonlarning kubini chiqaruvchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# for son in range(1, n + 1):
#     kub = son ** 3
#     print(f"{son} ning kubi: {kub}")



#             masala 8
# for8: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha butun sonlarning yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(1, n + 1):
#     yigindi += son
# print(f"1 dan {n} gacha bo'lgan sonlarning yig'indisi: {yigindi}")
    
    
#             masala 9
# for9: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha juft sonlarning yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(2, n + 1, 2):
#     yigindi += son
# print(f"1 dan {n} gacha bo'lgan juft sonlarning yig'indisi: {yigindi}")

#             masala 10
# for10: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha toq sonlarning yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(1, n + 1, 2):
#     yigindi += son
# print(f"1 dan {n} gacha bo'lgan toq sonlarning yig'indisi: {yigindi}")


#             masala 11
# for11: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha sonlarning ko'paytmasini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# kopaytma = 1
# for son in range(1, n + 1):
#     kopaytma *= son
# print(f"1 dan {n} gacha bo'lgan sonlarning ko'paytmasi: {kopaytma}")


#             masala 12
# for12: n butun son berilgan (n>0). n! ni hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# faktorial = 1
# for son in range(1, n + 1):
#     faktorial *= son
# print(f"{n}! ning qiymati: {faktorial}")


#             masala 13
# for13: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha sonlarning kvadratlar yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(1, n + 1):
#     yigindi += son ** 2
# print(f"1 dan {n} gacha bo'lgan sonlarning kvadratlar yig'indisi: {yigindi}")


#             masala 14
# for14: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha sonlarning kubar yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(1, n + 1):
#     yigindi += son ** 3
# print(f"1 dan {n} gacha bo'lgan sonlarning kubar yig'indisi: {yigindi}")


#             masala 15
# for15: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha juft sonlarning kvadratlar yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(2, n + 1, 2):
#     yigindi += son ** 2
# print(f"1 dan {n} gacha bo'lgan juft sonlarning kvadratlar yig'indisi: {yigindi}")


#             masala 16
# for16: n butun son berilgan (n>0). 1 dan n gacha bo'lgan barcha toq sonlarning kubar yig'indisini hisoblovchi programma tuzilsin.
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(1, n + 1, 2):
#     yigindi += son ** 3
# print(f"1 dan {n} gacha bo'lgan toq sonlarning kubar yig'indisi: {yigindi}")
