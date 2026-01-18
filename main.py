

# 1a - Svar i timmar
distance = 470
speed = int(input("Ange Hastighet i km/h: "))
#speed_int = int(speed)
time_in_hours = distance / speed
print("Det tar " + str(time_in_hours) + "h")

# 1b - Svar i minuter
distance = 470
speed = int(input("Ange Hastighet i km/h: "))
#speed_int = int(speed)
time_in_hours = distance / speed
time_in_minutes = time_in_hours * 60
print("Det tar " + str(time_in_minutes) + "min")

# 1c - Svar i timmar och minuter
distance = 470
speed = int(input("Ange Hastighet i km/h: "))
minutes = int(distance / speed * 60)
time_in_hours = minutes // 60
time_in_minutes = minutes % 60
print("Det tar " + str(time_in_hours) + " timmar och " + str(time_in_minutes) + " minuter")

import math

# 2 Hypotenusan
x = int(input("Ange ena kortsidan av triangeln: "))
ena_kortsida = x * x
z = int(input("Ange andra kortsidan av triangeln: "))
andra_kortsida = z * z
hypotenusan = ena_kortsida + andra_kortsida
hypotenusan = int(math.sqrt(hypotenusan))
print(hypotenusan)