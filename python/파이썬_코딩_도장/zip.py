t='12345678'
for i,j,k in zip( t[i:] for i in range(3) ):
    print(i,j,k)