import tkinter as tk  # Mengimpor modul Tkinter untuk membuat GUI

# Fungsi yang menampilkan hasil prediksi prodi
def hasil_prediksi():
    # Menulis "Teknologi Informasi" ke dalam label hasil prediksi
    result_label.config(text="Prodi: Teknologi Informasi")

# Membuat jendela utama untuk aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Memberikan judul pada jendela utama
root.geometry('400x500')  # Menentukan ukuran jendela (lebar x tinggi)

# Membuat label judul untuk aplikasi
judul_label = tk.Label(root,
                       text='Prediksi Program Studi',
                       font=('Arial', 16, 'bold'),  # Mengatur font dan ukurannya
                       fg='#007bff')  # Mengatur warna teks menjadi biru
judul_label.pack(pady=20)  # Menambahkan padding atas dan bawah pada label judul

# Frame untuk mengelompokkan input nilai mata pelajaran
input_frame = tk.Frame(root)
input_frame.pack(pady=10)  # Menambahkan padding atas dan bawah pada frame

# Membuat input untuk nilai mata pelajaran
nilai_entries = []  # Menyimpan entry input dalam daftar untuk kemudahan akses

for i in range(10):  # Loop untuk membuat 10 input nilai
    # Membuat label untuk setiap nilai mata pelajaran
    label_nilai = tk.Label(input_frame, text=f'Nilai {i+1}:', width=15, anchor=tk.W)
    # Membuat entry (kotak input) untuk setiap nilai
    entry_nilai = tk.Entry(input_frame, width=10)
    
    # Menempatkan label dan entry dalam grid, dengan padding di setiap sisi
    label_nilai.grid(row=i, column=0, padx=5, pady=5)
    entry_nilai.grid(row=i, column=1, padx=5, pady=5)
    
    # Menambahkan entry ke dalam daftar untuk referensi nanti
    nilai_entries.append(entry_nilai)

# Membuat tombol untuk menampilkan hasil prediksi
button_hasil_prediksi = tk.Button(root,
                                  text='Hasil Prediksi',  # Teks pada tombol
                                  command=hasil_prediksi)  # Menghubungkan tombol ke fungsi hasil_prediksi
button_hasil_prediksi.pack(pady=20)  # Menambahkan padding di bawah tombol

# Membuat label untuk menampilkan hasil prediksi
result_label = tk.Label(root,
                        text='',  # Teks awal kosong
                        font=('Arial', 14),  # Mengatur font dan ukuran teks
                        fg='#007bff')  # Mengatur warna teks menjadi biru
result_label.pack(pady=10)  # Menambahkan padding atas pada label hasil

# Menjalankan aplikasi, menampilkan GUI di layar
root.mainloop()
