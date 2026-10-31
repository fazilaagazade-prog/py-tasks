yas = int(input("Yasinizi daxil edin: "))
telebe = input("Telebesinizmi? (beli / xeyr): ").strip().lower()
if yas < 7:
    print("Bilet pulsuzdur (0 AZN)")
elif yas > 65:
    print("Bilet qiymeti: 4 AZN")
elif telebe == "bəli":
    print("Bilet qiymeti: 5 AZN")
else:
    print("Bilet qiymeti: 8 AZN")          