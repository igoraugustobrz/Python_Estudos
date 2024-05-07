#  Modifique o programa do método bolha para ordenar a lista em ordem decrescente. L = [1, 2, 3, 4, 5]
# deve ser ordenada como L = [5, 4, 3, 2, 1]
l = [1, 2, 3, 4, 5]
for x in range(len(l)):
    for y in range(len(l) - 1):
        if l[y] < l[y + 1]:
            temp = l[y]
            l[y] = l[y + 1]
            l[y + 1] = temp
print(l)