ceki = float(input("Camadanin çekisini daxil edin (kq): "))
bilet_novu = input("Bilet novunu daxil edin (econom / business): ").strip().lower()
if ceki > 32:
    print("Camadan 32 kq-dan agir oldugu ucun hec bir biletle qebul edilmir.")
elif bilet_novu == "econom":
    if ceki <= 23:
        print("Baqaj pulsuzdur.")
    else:  
        print("Elave odeniş: 30 AZN.")
elif bilet_novu == "business":
    if ceki <= 32:
        print("Baqaj pulsuzdur.")
else:
    print("Yanlis bilet novu daxil edildi. Zehmet olmasa 'econom' ve ya 'business' yazin.")