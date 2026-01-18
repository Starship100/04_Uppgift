

# 1a
distance = 470
speed = int(input("Ange Hastighet i km/h: "))
#speed_int = int(speed)
time_in_hours = distance / speed
print("Det tar " + str(time_in_hours) + "h")

# 1b
distance = 470
speed = int(input("Ange Hastighet i km/h: "))
#speed_int = int(speed)
time_in_hours = distance / speed
time_in_minutes = time_in_hours * 60
print("Det tar " + str(time_in_minutes) + "min")

# 1c
distance = 470
speed = int(input("Ange Hastighet i km/h: "))
minutes = int(distance / speed * 60)
time_in_hours = minutes // 60
time_in_minutes = minutes % 60
print("Det tar " + str(time_in_hours) + " timmar och " + str(time_in_minutes) + " minuter")

# 2