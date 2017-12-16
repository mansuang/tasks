import time
# รับค่า Q
# Q = int(input("Enter Q: "))

# Loop รับค่า n แต่ละตัวและเก็บเป็น list
ns = []
# for x in range(0, Q):
#     ns.append(int(input("Enter n(%d): " % (x+1))))
print(time.strftime("%H:%M:%S"))

Q = 301
for x in range(1, Q):
    ns.append(x)
# Loop คิดแต่ละ n
for n in ns:
    total = 0
    for i in range(1, n+1):
        for j in range(1, n+i+1):
            for k in range(1, n+i+j+1):            
                ctotal = (i*j*k)%(i+j+k)
                # print("i= %d, j=%d, k=%d, %d=(%d)mod(%d)" % (i, j, k, ctotal, (i*j*k), (i+j+k)))
                total += ctotal
    with open("p0043.txt", "a") as resultFile:
        resultFile.write("%d=%d\n" % (n, total))
    print("f(%d)=%d" % (n, total))

print(time.strftime("%H:%M:%S"))
