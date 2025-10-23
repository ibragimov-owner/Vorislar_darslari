import math

   
# ism = input("ismingiz nima? :")
# print("assalomu alaykum hurmatli, kelajagi buyuk", ism)


# son = int(input("ixtiyoriy son kiriting: "))
# print("kiritilgan sonning kvadrati", son*son)

# son = int(input("ixtiyoriy son kiriting: "))
# print(f"{son} ning kvadrati {son**2} ga teng")





# 8. Ikkita son a va b berilgan. Ularning o'rta arifmetigi aniqlansin. (a+b)/2
a = int(input("a="))
b = int(input("b="))
orta_arifmetik = (a + b ) / 2

print("O‘rta arifmetik =", orta_arifmetik)


# 17.Sonlar o'qida A, B, C nuqtalar berilgan. AC va BC kesmalarning uzunligini va kesmalar uzunligining yig'indisini topuvchi programma tuzilsin.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

AC = A * C
BC = B * C
yigindi = AC + BC

print("AC + BC =", yigindi)





# 26.
x = int(input("x = "))
y = 4 * (x-3)**6 - 7 * (x-3)**3 + 2
print("y =", y)
# 27. Doiraning radiusi berilgan. Uning uzunligini va yuzasini topuvchi programma tuzilsin.
r = float(input("Doiraning radiusini kiriting: "))
uzunlik = 2 * math.pi * r
yuzasi = math.pi * r**2
print("Doiraning uzunligi:", uzunlik)
print("Doiraning yuzasi:", yuzasi)

# 28. To'g'ri to'rtburchakning ikki tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.

a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))
b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))
perimetri = 2 * (a + b)
yuzasi = a * b
print("To'g'ri to'rtburchakning perimetri:", perimetri)
print("To'g'ri to'rtburchakning yuzasi:", yuzasi)
# 29. Teng yonli uchburchakning tomonlari berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng yonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng yonli uchburchakning perimetri:", perimetri)
print("Teng yonli uchburchakning yuzasi:", yuzasi)
# 30. Kvadratning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Kvadratning tomonini kiriting: "))
perimetri = 4 * a
yuzasi = a**2
print("Kvadratning perimetri:", perimetri)
print("Kvadratning yuzasi:", yuzasi)
# 31. Teng tomonli uchburchakning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng tomonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng tomonli uchburchakning perimetri:", perimetri)
print("Teng tomonli uchburchakning yuzasi:", yuzasi)
# 32. Doiraning radiusi berilgan. Uning uzunligini va yuzasini topuvchi programma tuzilsin.
r = float(input("Doiraning radiusini kiriting: "))
uzunlik = 2 * math.pi * r
yuzasi = math.pi * r**2
print("Doiraning uzunligi:", uzunlik)
print("Doiraning yuzasi:", yuzasi)
# 33. To'g'ri to'rtburchakning ikki tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))  
b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))
perimetri = 2 * (a + b)
yuzasi = a * b
print("To'g'ri to'rtburchakning perimetri:", perimetri)
print("To'g'ri to'rtburchakning yuzasi:", yuzasi)
# 34. Kvadratning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Kvadratning tomonini kiriting: "))
perimetri = 4 * a
yuzasi = a**2
print("Kvadratning perimetri:", perimetri)
print("Kvadratning yuzasi:", yuzasi)
# 35. Teng yonli uchburchakning tomonlari berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng yonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng yonli uchburchakning perimetri:", perimetri)
print("Teng yonli uchburchakning yuzasi:", yuzasi)
# 36. Teng tomonli uchburchakning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng tomonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng tomonli uchburchakning perimetri:", perimetri)
print("Teng tomonli uchburchakning yuzasi:", yuzasi)
# 37. Doiraning radiusi berilgan. Uning uzunligini va yuzasini topuvchi programma tuzilsin.
r = float(input("Doiraning radiusini kiriting: "))
uzunlik = 2 * math.pi * r
yuzasi = math.pi * r**2
print("Doiraning uzunligi:", uzunlik)
print("Doiraning yuzasi:", yuzasi)
# 38. To'g'ri to'rtburchakning ikki tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))
b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))
perimetri = 2 * (a + b)
yuzasi = a * b
print("To'g'ri to'rtburchakning perimetri:", perimetri)
print("To'g'ri to'rtburchakning yuzasi:", yuzasi)
# 39. Kvadratning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Kvadratning tomonini kiriting: "))
perimetri = 4 * a
yuzasi = a**2
print("Kvadratning perimetri:", perimetri)
print("Kvadratning yuzasi:", yuzasi)
# 40. Teng yonli uchburchakning tomonlari berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng yonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng yonli uchburchakning perimetri:", perimetri)
print("Teng yonli uchburchakning yuzasi:", yuzasi)
# 41. Teng tomonli uchburchakning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng tomonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng tomonli uchburchakning perimetri:", perimetri)
print("Teng tomonli uchburchakning yuzasi:", yuzasi)
# 42. Doiraning radiusi berilgan. Uning uzunligini va yuzasini topuvchi programma tuzilsin.
r = float(input("Doiraning radiusini kiriting: "))
uzunlik = 2 * math.pi * r
yuzasi = math.pi * r**2
print("Doiraning uzunligi:", uzunlik)
print("Doiraning yuzasi:", yuzasi)
# 43. To'g'ri to'rtburchakning ikki tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))
b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))
perimetri = 2 * (a + b)
yuzasi = a * b
print("To'g'ri to'rtburchakning perimetri:", perimetri)
print("To'g'ri to'rtburchakning yuzasi:", yuzasi)
# 44. Kvadratning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Kvadratning tomonini kiriting: "))
perimetri = 4 * a
yuzasi = a**2
print("Kvadratning perimetri:", perimetri)
print("Kvadratning yuzasi:", yuzasi)
# 45. Teng yonli uchburchakning tomonlari berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng yonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng yonli uchburchakning perimetri:", perimetri)
print("Teng yonli uchburchakning yuzasi:", yuzasi)
# 46. Teng tomonli uchburchakning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng tomonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng tomonli uchburchakning perimetri:", perimetri)
print("Teng tomonli uchburchakning yuzasi:", yuzasi)
# 47. Doiraning radiusi berilgan. Uning uzunligini va yuzasini topuvchi programma tuzilsin.
r = float(input("Doiraning radiusini kiriting: "))
uzunlik = 2 * math.pi * r
yuzasi = math.pi * r**2
print("Doiraning uzunligi:", uzunlik)
print("Doiraning yuzasi:", yuzasi)
# 48. To'g'ri to'rtburchakning ikki tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))
b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))
perimetri = 2 * (a + b)
yuzasi = a * b
print("To'g'ri to'rtburchakning perimetri:", perimetri)
print("To'g'ri to'rtburchakning yuzasi:", yuzasi)
# 49. Kvadratning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Kvadratning tomonini kiriting: "))
perimetri = 4 * a
yuzasi = a**2
print("Kvadratning perimetri:", perimetri)
print("Kvadratning yuzasi:", yuzasi)
# 50. Teng yonli uchburchakning tomonlari berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng yonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2
print("Teng yonli uchburchakning perimetri:", perimetri)
print("Teng yonli uchburchakning yuzasi:", yuzasi)
# 51. Teng tomonli uchburchakning tomoni berilgan. Uning perimetri va yuzasini topuvchi programma tuzilsin.
a = float(input("Teng tomonli uchburchakning tomonini kiriting: "))
perimetri = 3 * a
yuzasi = (math.sqrt(3) / 4) * a**2



