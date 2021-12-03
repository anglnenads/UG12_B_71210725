n = input("Masukkan nama : ")

p=[]
q=[]

while n != "STOP":
    a= "Masukkan nomor kursi "+n+" :"
    b = input(a)

    if b not in p:
        p.append(b)
        q.append(n)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")

    n =input("Masukkan nama :")

print()
print("List kursi yang telah terisi :")

for i in range(len(p)):
    print("kursi nomor %s telah diisi oleh %s" %(p[i],q[i]))