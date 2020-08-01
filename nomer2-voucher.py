def main():
    JumlahUang = int(input("Jumlah Uang kaka : "))
    JumlahDibayar = int(input("Jumlah Yang Harus di Bayar kaka : "))
    diskon = 0
    cek(JumlahUang,JumlahDibayar,diskon)
    
def cek(JumlahUang,JumlahDibayar,diskon):
    if JumlahUang >= 80000:
        lebihdelapanpuluh(JumlahUang,JumlahDibayar,diskon)
    else:
        print('Jumlah Uang Melebihi')

def lebihdelapanpuluh(JumlahUang,JumlahDibayar,diskon):
    diskon = 0.30
    kalkulasidiskon = 80000 / 0.30
    Hasil = JumlahUang - kalkulasidiskon
    print('Discount :'  % kalkulasidiskon)


main()