a = int(input())
b = int(input())
result1 = a * (b%10)
result2 = a * ((b%100)//10)
result3 = a * (b//100)
result4 = a * b
print(result1, result2, result3, result4, sep='\n')
