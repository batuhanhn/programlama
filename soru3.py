def hesapla():
    ilk_yaz_gelir=10000
    ilk_fin_gelir=5000
    ilk_ürün_gelir=15000
    ilk_altiay_gelir=ilk_yaz_gelir+ilk_fin_gelir+ilk_ürün_gelir
    print(ilk_altiay_gelir)
    
    ilk_cal_maas=5000
    ilk_kira_gider=1000
    ilk_don_maliyet=2000
    ilk_altiay_gider=ilk_cal_maas+ilk_kira_gider+ilk_don_maliyet
    print(ilk_altiay_gider)
    
    ilk_kar= ilk_altiay_gelir-ilk_altiay_gider
    print(ilk_kar)

    son_yaz_gelir=10000
    son_spo_gelir=5000
    son_ürün_gelir=15000
    son_etic_gelir=5000
    son_altiay_gelir=son_yaz_gelir+son_spo_gelir+son_ürün_gelir+son_etic_gelir
    print(son_altiay_gelir)

    son_cal_maas=6000
    son_kira_gider=2000
    son_bak_maliyet=3000
    son_altiay_gider=son_cal_maas+son_kira_gider+son_bak_maliyet
    print(son_altiay_gider)
    son_kar= son_altiay_gelir-son_altiay_gider
    print(son_kar)
    fark=son_kar-ilk_kar
    if fark>5000:
        print("işletme çok karlı")
    elif 1000<fark<5000:
        print("işletma kari normal")
    else:
        print("işletme yeterince karda değil")
hesapla()
