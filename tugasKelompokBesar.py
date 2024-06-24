def bubble_sort(items):
    n = len(items)
    # Lakukan iterasi sebanyak n-1 kali
    for i in range(n-1):
        # Dalam setiap iterasi, bandingkan dan tukar elemen
        for j in range(0, n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

# Contoh daftar belanja
daftar_belanja = ["buah", "kopi", "coklat"]

print("Daftar belanja sebelum diurutkan:", daftar_belanja)

# Panggil fungsi bubble_sort untuk mengurutkan
bubble_sort(daftar_belanja)

print("Daftar belanja setelah diurutkan:", daftar_belanja)