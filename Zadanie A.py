thislist = ["jablko", "gruszka", "banan", "pomarancza", "banan", "jablko"]
print("Zawartosc listy: ",thislist)
ilosc_slow = len(thislist)
print("Ilosc slow w liscie: ",ilosc_slow)
posortowana = sorted(thislist)
print("Posortowana lista alfabetycznie: ", posortowana)
jablko_count = thislist.count("jablko")
gruszka_count = thislist.count("gruszka")
banan_count = thislist.count("banan")
pomarancza_count = thislist.count("pomarancza")
print("{} wystapien".format(jablko_count))
print("{} wystapien".format(gruszka_count))
print("{} wystapien".format(banan_count))
print("{} wystapien".format(pomarancza_count))
