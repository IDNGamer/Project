import random

def tentukan_pemenang(pemain, komputer):
    if pemain == komputer:
        return "seri"
    elif (pemain == 'batu' and komputer == 'gunting') or \
         (pemain == 'gunting' and komputer == 'kertas') or \
         (pemain == 'kertas' and komputer == 'batu'):
        return "pemain"
    else:
        return "komputer"

def main():
    pilihan = ['batu', 'gunting', 'kertas']
    skor_pemain = 0
    skor_komputer = 0
    ronde = 1

    print("Selamat datang di permainan Batu Gunting Kertas!")
    print("Ketik 'keluar' untuk mengakhiri permainan.\n")

    while True:
        print(f"--- Ronde {ronde} ---")
        pemain = input("Pilih (batu/gunting/kertas): ").lower()

        if pemain == 'keluar':
            print("\nPermainan selesai.")
            break

        if pemain not in pilihan:
            print("Pilihan tidak valid. Coba lagi.\n")
            continue

        komputer = random.choice(pilihan)
        print(f"Komputer memilih: {komputer}")

        hasil = tentukan_pemenang(pemain, komputer)

        if hasil == "seri":
            print("Hasil: Seri!")
        elif hasil == "pemain":
            print("Hasil: Kamu menang!")
            skor_pemain += 1
        else:
            print("Hasil: Kamu kalah!")
            skor_komputer += 1

        print(f"Skor Sementara -> Kamu: {skor_pemain} | Komputer: {skor_komputer}\n")
        ronde += 1

    print(f"\nSkor Akhir -> Kamu: {skor_pemain} | Komputer: {skor_komputer}")
    if skor_pemain > skor_komputer:
        print("🎉 Kamu menang keseluruhan!")
    elif skor_pemain < skor_komputer:
        print("💻 Komputer menang keseluruhan!")
    else:
        print("🤝 Permainan berakhir seri!")

if __name__ == "__main__":
    main()
