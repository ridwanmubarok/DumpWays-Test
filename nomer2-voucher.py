def main():
    JumlahUang = int(input("Uang kaka Rp.: "))
    cek(JumlahUang)
    
def cek(JumlahUang):
    if JumlahUang >= 80000:
        JumlahDibayar = int(input("Yang Harus di Bayar kaka Rp. : "))
        lebihdelapanpuluh(JumlahDibayar,JumlahUang)
    elif JumlahUang >= 50000:
        JumlahDibayar = int(input("Yang Harus di Bayar kaka Rp. : "))
        lebihlimapuluh(JumlahDibayar,JumlahUang)

def lebihdelapanpuluh(JumlahDibayar,JumlahUang):
    diskon = 0.30
    kalkulasidiskon = JumlahDibayar * diskon
    hasil = JumlahDibayar - kalkulasidiskon
    kembalian = JumlahUang - hasil 
    print("---HASIL PERHITUNGAN---")
    print("Diskon : Rp. %s" % diskon)
    print("Diskon : Rp. %s" % kalkulasidiskon)
    print("Jumlah Dibayar : Rp. %s" % JumlahDibayar)
    print("Total Pembayaran  : Rp. %s" % hasil)
    print("Kembalian  : Rp. %s" % kembalian)

def lebihlimapuluh(JumlahDibayar,JumlahUang):
    diskon = 0.21
    kalkulasidiskon = JumlahDibayar * diskon
    hasil = JumlahDibayar - kalkulasidiskon
    kembalian = JumlahUang - hasil 
    print("---HASIL PERHITUNGAN---")
    print("Diskon : Rp. %s" % diskon)
    print("Diskon : Rp. %s" % kalkulasidiskon)
    print("Jumlah Dibayar : Rp. %s" % JumlahDibayar)
    print("Total Pembayaran  : Rp. %s" % hasil)
    print("Kembalian  : Rp. %s" % kembalian)


main()