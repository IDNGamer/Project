import tkinter as tk
import random

# Global skor
pemain_skor = 0
komputer_skor = 0

pilihan = ['batu', 'gunting', 'kertas']

def main_game(pemain_pilihan):
    global pemain_skor, komputer_skor
    
    komputer_pilihan = random.choice(pilihan)
    hasil = ""

    if pemain_pilihan == komputer_pilihan:
        hasil = "Seri!"
    elif (pemain_pilihan == 'batu' and komputer_pilihan == 'gunting') or \
         (pemain_pilihan == 'gunting' and komputer_pilihan == 'kertas') or \
         (pemain_pilihan == 'kertas' and komputer_pilihan == 'batu'):
        hasil = "Kamu Menang!"
        pemain_skor += 1
    else:
        hasil = "Kamu Kalah!"
        komputer_skor += 1

    hasil_label.config(text=f"Hasil: {hasil}")
    pilihan_label.config(text=f"Komputer memilih: {komputer_pilihan}")
    skor_label.config(text=f"Skor - Kamu: {pemain_skor} | Komputer: {komputer_skor}")

# GUI setup
root = tk.Tk()
root.title("Batu Gunting Kertas")

judul = tk.Label(root, text="Permainan Batu Gunting Kertas", font=("Helvetica", 16, "bold"))
judul.pack(pady=10)

hasil_label = tk.Label(root, text="Pilih salah satu untuk mulai bermain!", font=("Helvetica", 12))
hasil_label.pack(pady=5)

pilihan_label = tk.Label(root, text="", font=("Helvetica", 12))
pilihan_label.pack(pady=5)

skor_label = tk.Label(root, text="Skor - Kamu: 0 | Komputer: 0", font=("Helvetica", 12))
skor_label.pack(pady=10)

frame_tombol = tk.Frame(root)
frame_tombol.pack(pady=10)

btn_batu = tk.Button(frame_tombol, text="Batu", width=10, command=lambda: main_game('batu'))
btn_batu.grid(row=0, column=0, padx=5)

btn_gunting = tk.Button(frame_tombol, text="Gunting", width=10, command=lambda: main_game('gunting'))
btn_gunting.grid(row=0, column=1, padx=5)

btn_kertas = tk.Button(frame_tombol, text="Kertas", width=10, command=lambda: main_game('kertas'))
btn_kertas.grid(row=0, column=2, padx=5)

btn_keluar = tk.Button(root, text="Keluar", command=root.quit)
btn_keluar.pack(pady=10)

root.mainloop()
