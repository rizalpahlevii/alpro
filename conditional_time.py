hour = int(input("Jam  : "))
if 7 <= hour < 12:
    greeting = "Selamat Pagi"
elif 12 <= hour < 15:
    greeting = "Selamat Siang"
elif 16 <= hour < 18:
    greeting = "Selamat Sore"
else:
    greeting = "Selamat Malam"

print("{}!".format(greeting))
