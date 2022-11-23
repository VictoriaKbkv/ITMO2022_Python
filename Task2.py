string1 = "This is a string."
string2 = " This is another string."

print(string1 + string2)
print(f"Длина строки: {len(string2)} символа")
print(f"Первый символ каждого слова в верхнем регистре: {string1.title()}")
print(f"Все символы в нижнем регистре: {string1.lower()}")
print(f"Все символы в верхнем регистре: {string1.upper()}")
print(f"Без пробелов в начале строки: {string2.lstrip()}")
print(f"Без пробелов в конце строки: {string2.rstrip()}")
print(f"Без пробелов в начале и в конце строки: {string2.strip()}")
print(f"Удаляются с обоих концов строки указанные символы: {string2.strip('.')}")

print()

print(string1[2])  # Индексация с 0
print(string1[1:3])  # [i:j] символ с индексом j не включается
print(string1[1:])  # [i:j] с символа i до конца строки
print(string1[:3])  # Указанное кол-во символов с начала строки
print(string1[:])  # Вся строка
print(string1[1:5:2])  # [begin:end:step] end - не включается

print()

a = 5
b = 3
print(a // b)
print(a % b)
print(a ** b ** b)
print((a ** b) ** b)
