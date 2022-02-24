array = []
total = 0
n = int(input("masukkan jumlah elemen array :"))
for x in range(n):
    nilai =float(input("masukkan nilai ke- {} :".format(x+1)))
    array.append(nilai)
    print("\n hasil nilai total adalah : {}".format(sum(array)))
    print("hasil rata-rata adalah : {}".format(sum(array)/n))