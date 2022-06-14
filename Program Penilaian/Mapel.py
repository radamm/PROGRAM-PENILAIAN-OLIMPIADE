from prettytable import PrettyTable

class Mapel:
    def __init__(self, nama_mapel):
        self.mapel = nama_mapel

    def info(self):
        print(' Mata Pelajaran\t: %s' %(self.mapel))
    

class Kategori(Mapel):
    def __init__(self, skor_benar, skor_salah, skor_kosong, jumlah_benar, jumlah_salah, jumlah_kosong):
        self.sbenar = skor_benar
        self.ssalah = skor_salah
        self.skosong= skor_kosong
        self.Benar  = jumlah_benar
        self.Salah  = jumlah_salah
        self.Kosong = jumlah_kosong    

    def info(self):
        print("==========================================")
        tabelSiswa = PrettyTable(["Kriteria Penilaian","Perolehan Jawaban"])
        tabelSiswa.add_row(["Skor Benar = %i" %(self.sbenar), "Jawaban Benar = %i" %(self.Benar)])
        tabelSiswa.add_row(["Skor Salah = %i" %(self.ssalah), "Jawaban Salah = %i" %(self.Salah)])
        tabelSiswa.add_row(["Skor Kosong= %i" %(self.skosong), "Jawaban Kosong= %i" %(self.Kosong)])
        print(tabelSiswa)

    def nilai(self):
        print("==========================================")
        print("Skor Final yang Diperoleh")
        print(" Skor Akhir Benar\t\t= %i\n Skor Akhir Salah\t\t= %i\n Skor Akhir Tidak Dijawab\t= %i" %(self.Benar, self.Salah, self.Kosong))
        print("-------------------------------------- +")
        score = self.Benar*self.sbenar + self.Salah*self.ssalah + self.Kosong*self.skosong
        print(" Total Score\t\t\t= %i" %(score))

        
