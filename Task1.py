import math

FEET_PER_YARD = 3
FEET_PER_MILE = 5280
DEGREES_PER_RADIAN = 57.2958
SEC_PER_HOUR = 3600

def time_to_save(d1, d2, h, V_sand, n, theta1):
    L1 = d1 / math.cos(theta1)
    L2 = math.sqrt((h - L1 * math.sin(theta1)) ** 2 + d2 ** 2)
    t = (L1 + n * L2) / V_sand
    return t


d1 = float(input("Кратчайшее расстояние от спасателя до кромки воды, 𝑑1 (в ярдах): ")) * FEET_PER_YARD
d2 = float(input("Кратчайшее расстояние от утопающего до берега, 𝑑2 (в футах): "))
h = float(input("Боковое смещение между спасателем и утопающим, ℎ (в ярдах): ")) * FEET_PER_YARD
V_sand = float(input("Скорость движения спасателя по песку, V𝑠𝑎𝑛𝑑 (в милях в час): ")) * FEET_PER_MILE / SEC_PER_HOUR
n = float(input("Коэффициент замедления спасателя при движении в воде, n (в ед.): "))
theta1 = float(input("Направление движения спасателя по песку, 𝜃1 (в градусах): ")) / DEGREES_PER_RADIAN
print(f"Cпасатель достигнет утопащего через {time_to_save(d1, d2, h, V_sand, n, theta1): .2f} секунд(ы)")
