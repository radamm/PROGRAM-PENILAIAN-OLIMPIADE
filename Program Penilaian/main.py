from Mapel import Mapel
from Data_Peserta import Data_Peserta
from Mapel import Kategori
import os

def main():
    print("="*41)
    print("      PROGRAM  PENILAIAN  OLIMPIADE       ")
    print("="*41)
    nama = input("Masukkan Nama : ")
    askol = input("Masukkan Asal Sekolah : ")
    nomor = input("Masukkan Nomor Peserta : ")
    list = ["Matematika","Kimia","Fisika"]
    for x,option in enumerate(list):
            print(x+1, '. ', option)
    choice_mapel = int(input("Masukkan Cabang Olimpiade : "))
    if choice_mapel == 1:
        mapel = list[0]
    if choice_mapel == 2:
        mapel = list[1] 
    if choice_mapel == 3:
        mapel = list[2]
    os.system("cls")   
    
    print("======Ketentuan Penilaian Olimpiade %s======" %(mapel))
    nb = int(input("Masukkan skor per soal benar: "))
    ns = int(input("Masukkan skor per soal salah: "))
    nk = int(input("Masukkan skor per soal kosong: "))
    print("")
    print("======Perhitungan Skor======")
    sb = int(input("Masukkan Jumlah Soal Benar : "))
    ss = int(input("Masukkan Jumlah Soal Salah : "))
    sk = int(input("Masukkan Jumlah Soal Yang Tidak Dijawab : "))
    os.system("cls")

    dp  = Data_Peserta(nama, askol, nomor)
    mp  = Mapel(mapel)
    kat = Kategori(nb,ns,nk,sb,ss,sk)

    dp.info()
    mp.info()
    kat.info()
    kat.nilai()

main()    