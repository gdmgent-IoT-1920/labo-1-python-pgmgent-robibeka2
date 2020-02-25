import random


def kipEi_loop():
    userGuess = str(input(">>> "))
    kip = 0
    kipei = 0

    for i in range(4):
        if num[i] == userGuess[i]:
            kip += 1

    for i in num:
        if i in userGuess:
            kipei += 1

    ei = kipei - kip

    print("{} kip(pen), {} ei(eren)".format(kip, ei))

    return kip


if __name__ == '__main__':
    num = str(random.randrange(1000, 10000))

    print("LINGO-BINGO Welkom bij het kip en eieren spel!")
    print("Geef een viercijferig getal in:")
    kip = 0
    count = 0

    while kip != 4:
        count += 1
        kip = kipEi_loop()

    print("Je had {} poging(en) nodig".format(count))
