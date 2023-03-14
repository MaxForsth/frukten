import random
Frukter = ("Banan","Melon","kiwi","Citron")
Looping = True

def print_fruit(userinput):
    fnr = int(userinput):
    print("\n" + Frukter[fnr-1] + "kommer här! \n")

while Looping:
    Go = input("Vill du välja en frukt till? j/n")
    print("\n")

    if(Go == "n"):
        break