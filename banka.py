cardPinCode = "1431"
trying = 3

balance = 1000

print("Bankamıza Hoş Geldiniz.")

status = True
while status:
    if trying <= 0:
        print("Kartınız bloklandı. Banka ile görüşün.")
        status = False
    else:
        pinInput = input("Kart şifrenizi giriniz: ")
        if pinInput != cardPinCode:
            trying -= 1
            print("Yanlış şifre.", trying, "deneme hakkınız kaldı.", "Tekrar deneyiniz.")
        else:
            cardStatus = True
            print("Şifre doğru, giriş yapıldı.")
            print("""
                  İşlemler: 
                  1. Para Çekme
                  2. Para Yatırma
                  3. Bakiye Sorgulama
                  4. Çıkış
                """)
            while cardStatus:
                selectedOption = input("İşlem seçiniz: ")

                if selectedOption == "4":
                    print("Çıkış yapıldı.")
                    status = False
                    cardStatus = False
                elif selectedOption == "3":
                    print("Toplam bakiye:", balance,"₺")
                elif selectedOption == "2":
                    deposited = int(input("Ne kadar para yatıracaksınız?: "))
                    balance += deposited
                    print("Yatırıldı. Yeni bakiye:", balance,"₺")
                elif selectedOption == "1":
                    print("Bakiye:", balance, "₺")
                    withdrawn = int(input("Ne kadar para çekeceksiniz?: "))
                    newBalance = balance - withdrawn
                    isWithDrawnPossible = True if newBalance >= 0 else False
                    
                    if isWithDrawnPossible:
                        balance -= withdrawn
                        print("Çekildi. Yeni bakiye:", balance, "₺")
                    else:
                        print("Yeterli bakiye yok. Tekrar deneyiniz.")
                        print("Bakiye:", balance, "₺")
                else:
                    print("Yanlış işlem kodu. Tekrar deneyiniz.")
                    
                    
                

    

