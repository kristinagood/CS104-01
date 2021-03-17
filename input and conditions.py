temp = 0
temp = int(input("Please enter the current temperature or 999 to End: "))
if temp > 90:
    print ("wear shorts")
elif temp > 70:
    print ("short sleeves are fine")
elif temp > 50:
    print ("wear a jacket")
elif temp > 32:
    print ("wear a heavy coat")
elif temp <= 32:
    print ("stay inside")
