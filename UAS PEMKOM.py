#UAS PEMROGRAMAN KOMPUTER
#NAMA   : ADI NOVLY PARAPAT
#NIM    : 190402136

# Matriks ke-1
m1 = []
y = 0

print("program penjumlahan matriks sederhana")
print("--------------")
print("Matriks ke-1")
for x in range(3):
    print(f"Baris ke-{x + 1}")
    o =[]
    while y < 1:
        o.append(int(input("Data : ")))
        y = y + 1
    m1.append(o)
    y = 0
    x = x + 1

for o in m1:
    print(o)
print()


# Matriks ke-2
m2 = []
j = 0

print("Matriks ke 2")
for i in range(3):
    print(f"Baris ke-{i + 1}")
    p = []
    while j < 1:
        p.append(int(input("Data : ")))
        j = j + 1
    m2.append(p)
    j = 0
    i = i + 1
    print("data matriks ke 2")

for p in m2:
    print(p)
print()


#  o + p
print("Maka Penjumlahan Matriksnya adalah")
z = [[0], [0], [0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        z[i][j] = m1[i][j] + m2[i][j]

for t in z:
    print(t)
print()
print("Terima kasih, Semoga Bermanfaat")