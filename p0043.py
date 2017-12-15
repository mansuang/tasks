# รับค่า Q
Q = int(input("Enter Q: "))

# Loop รับค่า n แต่ละตัวและเก็บเป็น list
ns = []
for x in range(0, Q):
    ns.append(int(input("Enter n(%d): " % (x+1))))

# Loop คิดแต่ละ n
for n in ns:
    total = 0
    for i in range(1, n+1):
        for j in range(1, n+i+1):
            for k in range(1, n+i+j+1):
                total += (i*j*k)%(i+j+k)

    print("f(%d)=%d" % (n, total))
