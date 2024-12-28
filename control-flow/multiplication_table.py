number=int(input("Enter a number to see its multiplication table: "))
X=1
for X in range(1,11):
    Y=number
    Z=Y*X
    print(Y,"*",X,"=",Z)
    X=X+1

   