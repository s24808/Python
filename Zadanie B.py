try:
    num = input("Podaj liczbe: ")
    num = int(num)
    if (num % 2) == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")
except ValueError:
    print("Podana liczba nie jest calkowita")