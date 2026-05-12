def fibonacci(n):
    if n < 0: return 0
    if n == 1: return 1
    a, b = 0,1
    for _ in range(2, n + 1):
        a,b = b, a + b
    return b

#リスト作成
fib_list = []
for n in range(1,10):
    fib_list.append(fibonacci(n))
    
print(fib_list)