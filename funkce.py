#nejvyšší číslo
cisla = [20, -190, 56, 897, 5688, 4356]
nejvyssi_cislo = 0

for cislo in cisla:
    if nejvyssi_cislo == 0 or cislo > nejvyssi_cislo:
        nejvyssi_cislo = cislo
print("Nejvyšší číslo je", nejvyssi_cislo)