# buatlah program yang menghitung pajak.Dimana syarat minimum
# penghasilan untuk membayar pajak adalah Rp. 5.000.000, penghasilan bulanan
# di input dari keyboard. (jika penghasilan minimum terpengaruh maka besaran pajak adalah 
# 5% dari total penghasilan bulanan.)
penghasilan_bulanan=int(input("masukakan penghasilan bulanan : Rp "))
pajak=5/100
if penghasilan_bulanan >= 5000000:
    penghasilan_kotor = penghasilan_bulanan * 5/100
    penghasilan_bersih = penghasilan_bulanan - penghasilan_kotor
    print("penghasilan kotor : Rp ",penghasilan_kotor)
    print("penghasilan bersih: Rp ",penghasilan_bersih)
else : 
    print("penghasilan yang anda masukkan kurang dari 5.000.000")