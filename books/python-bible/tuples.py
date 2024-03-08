tup2 = ()

for i in range(1, 5):
    tup3 = ()
    for j in range (i):
        tup3 = tup3 + (j,)
        tup2 = tup2 + (tup3)

print(tup2)

