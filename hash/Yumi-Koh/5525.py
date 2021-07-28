n = int(input())
m = int(input())
p = 'I' + 'OI'*n
s = input()
result = 0
for i in range(0,len(s)-(2*n+1)):
    if s[i:i+(2*n+1)] == p:
        result += 1
print(result)