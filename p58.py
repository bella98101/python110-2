a1=int(input("請輸入第1個數字:"))
a2=int(input("請輸入第2個數字:"))
a3=int(input("請輸入第3個數字:"))
a4=int(input("請輸入第4個數字:"))
a5=int(input("請輸入第5個數字:"))
a6=int(input("請輸入第6個數字:"))
a7=int(input("請輸入第7個數字:"))
a8=int(input("請輸入第8個數字:"))
a9=int(input("請輸入第9個數字:"))
a10=int(input("請輸入第10個數字:"))
a=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
a.sort()
a.reverse()
print("最大的3個數字為:",a[0],a[1],a[2])
print("最小的3個數字為:",a[7],a[8],a[9])