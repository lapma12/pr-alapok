betuk = []
while True:
    betu = input("Adj meg betűket: ")
    if len(betu) == 2 or betu == "":
        break
    elif betu in betuk:
        print("Ezt a betűt már rögzítettem.")
    else:
        betuk.append(betu)
        print(f"Rögzített betűk: {sorted(betuk)}")