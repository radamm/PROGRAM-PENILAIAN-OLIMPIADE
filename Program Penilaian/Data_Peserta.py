class Data_Peserta:
    def __init__(self, nama, asal_sekolah, nomor_peserta):
        self.nama  = nama
        self.asal  = asal_sekolah
        self.nomor = nomor_peserta

    def info(self):
        print("="*41)
        print("    P E S E R T A    O L I M P I A D E    ")
        print("="*41)
        print(" Nama\t\t: %s\n Asal\t\t: %s\n Nomor Peserta\t: %s" %(self.nama, self.asal, self.nomor))
