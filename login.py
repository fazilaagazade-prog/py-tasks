DUZGUN_EMAIL = "fazile@gmail.com"
DUZGUN_SIFRE = "12345"
daxil_edilen_email = input("E-poçtunuzu daxil edin: ").strip()
daxil_edilen_sifre = input("Şifrənizi daxil edin: ").strip()
if daxil_edilen_email == DUZGUN_EMAIL and daxil_edilen_sifre == DUZGUN_SIFRE:
    print("Uğurlu giriş! Xoş gəldiniz.")
else:
    print("Xəta: Email və ya şifrə yanlişdir.")