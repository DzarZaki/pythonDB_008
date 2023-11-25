import tkinter as tk
import sqlite3

# Fungsi untuk menghitung dan menampilkan hasil prediksi
def hitung_prediksi():
    # Mendapatkan nilai dari input siswa
    nilai_biologi = float(input_frames[0].get())
    nilai_fisika = float(input_frames[1].get())
    nilai_inggris = float(input_frames[2].get())
    nama_siswa = input_frames[3].get()

    # Menentukan prodi berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_prodi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_prodi = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_prodi = "Bahasa"
    else:
        prediksi_prodi = "Belum dapat diprediksi"

    # Perbarui label keluaran dengan hasil prediksi
    luaran.config(text=f"Hasil Prediksi Prodi untuk {nama_siswa}: {prediksi_prodi}")

    # Simpan data ke SQLite
    simpan_data_ke_sqlite(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_prodi)

# Fungsi untuk menyimpan data ke SQLite
def simpan_data_ke_sqlite(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih):
    # Membuka atau membuat database SQLite
    conn = sqlite3.connect("prodidb.db")
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa TEXT,
                    nilai_biologi INTEGER, 
                    nilai_fisika INTEGER,
                    nilai_inggris INTEGER,
                    prodi_terpilih TEXT)''')

    # Memasukkan data nilai siswa ke dalam tabel
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih))

    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

# Buat jendela utama aplikasi Tkinter
uiApp = tk.Tk()

# Atur judul dan ukuran awal jendela
uiApp.title("Aplikasi Prediksi Prodi Pilihan")
uiApp.geometry("600x600")

# Label untuk judul aplikasi
judul = tk.Label(uiApp, text="Aplikasi Prediksi Prodi Pilihan")
judul.pack(pady=20)

# Buat 4 frame input untuk nilai mata pelajaran dan nama siswa
input_frames = []
label_texts = ["Nilai Biologi:", "Nilai Fisika:", "Nilai Inggris:", "Nama Siswa:"]
for i in range(4):
    # Label untuk setiap input mata pelajaran atau nama siswa
    label = tk.Label(uiApp, text=label_texts[i])
    label.pack()

    # Widget Entry untuk input nilai mata pelajaran atau nama siswa
    entry = tk.Entry(uiApp)
    entry.pack()

    # Tambahkan widget Entry ke dalam list input_frames
    input_frames.append(entry)

button_prediksi = tk.Button(uiApp, text="Hasil Prediksi", command=hitung_prediksi)
button_prediksi.pack(pady=20)

luaran = tk.Label(uiApp, text="", )
luaran.pack()

uiApp.mainloop()
