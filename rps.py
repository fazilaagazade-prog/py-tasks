oyuncu1 = input("1-ci oyunçu (das, qayci, kagiz): ").strip().lower()
oyuncu2 = input("2-ci oyunçu (das, qayci, kagiz): ").strip().lower()
kecerli_secimler = ["das", "qayci", "kagiz"]
if oyuncu1 not in kecerli_secimler or oyuncu2 not in kecerli_secimler:
    print("Bele secim yoxdur")
elif oyuncu1 == oyuncu2:
    print("Hec-hece!")
elif (oyuncu1 == "das" and oyuncu2 == "qayci") or \
     (oyuncu1 == "qayci" and oyuncu2 == "kagiz") or \
     (oyuncu1 == "kagiz" and oyuncu2 == "das"):
    print("1-ci oyunçu qalib geldi!")
else:
    print("2-ci oyuncu qalib geldi!")