n = input("Input : ")
print("Output : ")

lenght = len(n)

#upper triangle 
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" ",end="")

    for j in range(i+1):
        print(n[j],end="")

    print()

#lower triangle
for i in range(lenght-1):
    for j in range(i+1):
        print(" ",end="")

    for j in range(lenght-i-1):
        print(n[j],end="")
   
    print()
