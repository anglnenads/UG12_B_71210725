total_rows = int(input("Input : "))
print("Output : ")

for row in range(1, total_rows+1):
   for columns in range(1, total_rows+1):
      if row == total_rows or row+columns==total_rows+1 or columns==total_rows:
         print("*",end=" ")
      else:
         print(" ",end=" ")
   
   print()
