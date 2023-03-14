import random
Frukter = ("Banan","Melon","kiwi","Citron")
Looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + Frukter[fnr-1] + "\n kommer här! \n")



while Looping:

    print("------------------------")
    print("\n-: FruktAutomat:-\n")

    i=1

    for Frukt in Frukter:
        print(str(i) + ": " + Frukt)
        i += 1

    FruktNr = input("\\n Mata in nr på frukten du vill ha: ")

    print_fruit(FruktNr)

    Go = input("Vill du välja en frukt till? j/n")
    print("\n")

    if(Go == "n"):
        break

#Sluta ta på ,mig elloit

print("------")
print("Du får en frukt till")
Slumpfrukt = random.randint(1, 4)
print_fruit(Slumpfrukt)