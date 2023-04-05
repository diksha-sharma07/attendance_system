a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']

res = {a[i]:b[i] for i in range(len(a))}
print(res)