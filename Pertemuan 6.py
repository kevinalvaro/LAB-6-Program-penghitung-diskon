#by Kevin Alvaro Adianto

pilihan = "y"
while pilihan == "y":
    harga=float(input("Masukkan Harga Baju: "))
    member=input("Apakah Member? (y/t): ").lower()

    if harga >= 0 and harga < 100000:
        harga=harga
        if member == "y":
            harga=harga*90/100
        elif member == "t":
            harga=harga
        else:
            print("mohon memasukkan member dengan y atau t")
    elif harga >= 100000 and harga < 300000:
        harga=harga*85/100
        if member == "y":
            harga=harga*90/100
        elif member == "t":
            harga=harga
        else:
            print("mohon memasukkan member dengan y atau t")
    elif harga >= 300000:
        harga=harga*70/100
        if member == "y":
            harga=harga*90/100
        elif member == "t":
            harga=harga
        else:
            print("mohon memasukkan member dengan y atau t")
    else:
        print("Input Harga Out Of Range")
    
    print("harga setelah diskon adalah: ",harga)
    pilihan=input("Mau lagi? (y/t): ").lower()

print("Terima Kasih")