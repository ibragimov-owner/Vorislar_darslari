"""
04.11.2025
for sikl operatoriga oid masalalar:
For1. k va n butun sonlari berilgan (n > 0). k sonini n marta chiqaruvchi programma tuzilsin.
For2. a va b butun sonlari berilgan (a < b). a va b sonlari orasidagi barcha butun sonlami (a va b ni
ham) chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi programma tuzilsin. (a va b xam chiqarilsin).
For3. a va b butun sonlari berilgan (a <b). a va b sonlari orasidagi barcha butun sonlarni (a va b dan
tashqari) kamayish tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi progma tuzilsin.
For4. Bir kg konfetning narxi berilgan (haqiqiy son). 1, 2, ... , 10 kg konfetni narxini chiqaruvchi
programma tuzilsin.
For5. Bir kg konfetning narxi berilgan (haqiqiy son). 0.1, 0.2, ... , 0.9, 1 kg konfetni narxini chiqaruvchi
programma tuzilsin.
For6. Bir kg konfetning narxi berilgan (haqiqiy son). 1.2, 1.4, ... , 2 kg konfetni narxini chiqaruvchi
programma tuzilsin.
For7. a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini
chiqaruvchi programma tuzilsin.
For8. a va b butun sonlari berilgan (a <b). a dan b gacha bo'lgan barcha butun sonlar ko'paytmasini
chiqaruvchi programma tuzilsin.
For9. a va b butun sonlari berilgan (a <b). a dan b gacha bo'lgan barcha butun sonlar kvadratlarining
yig'indisini chiqaruvchi programma tuzilsin.
For11. n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin.
S =n2+(n+1)2+(n+2)2 + ... (2*n)2
For12. n butun soni berilgan (n >0). Quyidagi ko'paytmani hisoblovchi programma tuzilsin.
S=1.1*1.2*1.3 *...
(n ta ko'payuvchi)
For13. n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin.
S =1.1-1.2+1.3 -...+(-1)n+1 *1.n
"""

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
# narx = float(input("1 kg konfetning narxini kiriting: "))
# for kg in range(1, 11):
#     kg_kg = kg / 10
#     summa = kg_kg * narx
#     print(f"{kg_kg} kg konfetning narxi: {summa} so'm")



#         masala 6
# for6: Bir kg konfetning narxi berilgan (haqiqiy son). 1.2, 1.4, ... , 2 kg konfetni narxini chiqaruvchi programma tuzilsin.
# narx = float(input("1 kg konfetning narxini kiriting: "))
# for kg in range(12, 21, 2):
#     kg_kg = kg / 10
#     summa = kg_kg * narx
#     print(f"{kg_kg} kg konfetning narxi: {summa} so'm")   



#         masala 7
# for7: a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaruvchi programma tuzilsin.
# a = int(input("a sonini kiriting (a<b): "))
# b = int(input("b sonini kiriting (a<b): "))
# yigindi = 0  
# for son in range(a, b + 1):
#     yigindi += son
# print(f"{a} dan {b} gacha bo'lgan sonlar yig'indisi: {yigindi}")



#         masala 8
# for8: a va b butun sonlari berilgan (a <b). a dan b gacha bo'lgan barcha butun sonlar ko'paytmasini chiqaruvchi programma tuzilsin.
# a = int(input("a sonini kiriting (a<b): "))
# b = int(input("b sonini kiriting (a<b): "))
# kopaytma = 1
# for son in range(a, b + 1):
#     kopaytma *= son
# print(f"{a} dan {b} gacha bo'lgan sonlar ko'paytmasi: {kopaytma}")



#         masala 9
# for9: a va b butun sonlari berilgan (a <b). a dan b gacha bo'lgan barcha butun sonlar kvadratlarining yig'indisini chiqaruvchi programma tuzilsin.
# a = int(input("a sonini kiriting (a<b): "))
# b = int(input("b sonini kiriting (a<b): "))
# yigindi = 0
# for son in range(a, b + 1):
#     yigindi += son ** 2
# print(f"{a} dan {b} gacha bo'lgan sonlar kvadratlarining yig'indisi: {yigindi}")

#         masala 10
# for10: n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin.
# S =n2+(n+1)2+(n+2)2 + ... (2*n)2
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0
# for son in range(n, 2 * n + 1):
#     yigindi += son ** 2
# print(f"Yig'indi: {yigindi}")


#         masala 11
# for11: n butun soni berilgan (n >0). Quyidagi ko'paytmani hisoblovchi programma tuzilsin.
# S=1.1*1.2*1.3 *...
# (n ta ko'payuvchi)
# n = int(input("n sonini kiriting (n>0): "))
# kopaytma = 1.0
# for son in range(1, n + 1):
#     kopaytma *= 1 + son / 10
# print(f"Ko'paytma: {kopaytma}")


#         masala 12
# for12: n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin.
# S =1.1-1.2+1.3 -...+(-1)n+1 *1.n  
# n = int(input("n sonini kiriting (n>0): "))
# yigindi = 0.0
# for son in range(1, n + 1):
#     if son % 2 == 1:
#         yigindi += 1 + son / 10
#     else:
#         yigindi -= 1 + son / 10
# print(f"Yig'indi: {yigindi}")











