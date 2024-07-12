x = (2123, 432, 143, 657, 757, 344)
p = (3, 2, 7, 8, 9, 2)

somatorio = 0
somatorio_p = 0

for i, j in zip(x, p):
    somatorio += (i * j)
    somatorio_p += j
    
media_p = somatorio / somatorio_p
print(media_p)

x = (23, 45, 65, 76, 87, 23, 12, 43)
p = (8, 6, 4, 3, 2, 8, 9, 6)
somatorio = 0
somatorio_p = 0

for i, j in zip(x, p):
    somatorio += (i*j)
    somatorio_p += j
media_p = somatorio / somatorio_p

print(media_p)