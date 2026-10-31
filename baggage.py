ceki = float(input("Camadanin çekisini daxil edin (kq): "))
bilet_novu = input("Bilet novunu daxil edin (econom / business): ").strip().lower()
if ceki > 32:
    print("Camadan 32 kq-dan agir olduğu ucun hec bir biletlə qebul edilmir.")
elif bilet_novu == "econom":
    if ceki <= 23:
        print("Bağaj pulsuzdur.")
    else:  # 23 ile 32 kq arasi
        print("Elave odeniş: 30 AZN.")
elif bilet_novu == "business":
    if ceki <= 32:
        print("Bağaj pulsuzdur.")
else:
    print("Yanlis bilet novu daxil edildi. Zehmet olmasa 'econom' və ya 'business' yazin.")