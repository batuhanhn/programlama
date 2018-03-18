def stok():
    db_koltuk=50
    db_yatak=100
    db_dolap=70
    donembasi=db_koltuk+db_yatak+db_dolap
    print(donembasi)
    ds_koltuk=db_koltuk-25+10
    ds_yatak=db_yatak-20+15
    ds_dolap=db_dolap-10+5
    donemsonu=ds_koltuk+ds_yatak+ds_dolap
    print(donemsonu)
    ort_stok=( donembasi+donemsonu)/2
    print(ort_stok)
stok()
