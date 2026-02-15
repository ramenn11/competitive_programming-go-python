def tower(n, source, dest, aux):
    if n == 1:
        print(source, dest)
        return
    tower(n-1, source, aux, dest)
    print(source, dest)
    tower(n-1, aux, dest, source)
 
n = int(input())
print((1 << n) - 1)
tower(n, 1, 3, 2)