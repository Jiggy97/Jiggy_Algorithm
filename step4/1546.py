import numpy as np

n = int(input())
final = []

for i in range(n):
    point = int(input())
    print(end=" ")
    final.append(point)

best = max(final)

final = np.where(final == best, final, final/best*100)
print(np.mean(final))

