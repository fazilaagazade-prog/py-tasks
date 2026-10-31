mesafe = float(input("Mesafeni daxil edin (km): "))
saat = int(input("Saati daxil edin (0-23): "))
baslangic_qiymeti = 2.0
km_qiymeti = 0.80
hesablanan_qiymet = baslangic_qiymeti + (mesafe * km_qiymeti)
if saat >= 23 or saat <= 6:
    hesablanan_qiymet = hesablanan_qiymet * 1.20
if hesablanan_qiymet < 3.0:
    gedis_haqqi = 3.0
else:
    gedis_haqqi = hesablanan_qiymet
    print(f"Yekun gediş haqqi: {gedis_haqqi:.2f} AZN")