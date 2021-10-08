#membuat class
class RADIO:
    #fungsi construktor
    def __init__(self, nama_brand, ukuran_sound, jumlah_chanel):
        self.nama_brand = nama_brand
        self.ukuran_sound = ukuran_sound
        self.jumlah_chanel = jumlah_chanel

    #membuat fungsi dari RADIO
    def nyalakanRadio(self):
        print('Radio menyala ', self.nama_brand)

    def matikanRadio(self):
        print('Radio dimatikan ', self.nama_brand)

    def gantiChanelTambah(self):
        print('Radio gantichanel ', self.nama_brand)


#membuat objek
radio_ruang_kamar = RADIO('Polytron', '6.5', 10)
radio_ruang_tamu = RADIO('LG', '7', 15)
#memanggil fungsi dari objek
radio_ruang_kamar.nyalakanRadio()
radio_ruang_kamar

#memasukkan attribut ke objek
radio_ruang_kamar.nama_brand = 'Polytron'
radio_ruang_tamu.nama_brand = 'LG'

#print
print(radio_ruang_kamar.nama_brand)
print(radio_ruang_tamu.nama_brand)
