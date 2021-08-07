import sys

n = int(sys.stdin.readline())

i = 666
ans = 0
while True:
    if '666' in str(i):
        #print(i)
        ans += 1

    if ans == n:
        break

    i += 1

print(i)

# movies = []
# for i in range(10001):
#     movies.append(int(str(i)+ '666'))
#     movies.append(int('666' + str(i)))
#     movies.append(int(str(i)[:1]+ '666' + str(i)[1:]))
#     movies.append(int(str(i)[:2]+ '666' + str(i)[2:]))
#     movies.append(int(str(i)[:3]+ '666' + str(i)[3:]))
#     movies.append(int(str(i)[:4]+ '666' + str(i)[4:]))
    

# #print(movies)
# movies = list(set(movies))
# movies.sort()
# #print(movies[:100])
# print(movies[n-1])

# movies = []
# for i in range(n):
#     movies.append(int('666'+str(i)))
#     movies.append(int(str(i)+'666'))
#     movies.append(int(str(i)+'666'))

# movies = list(set(movies))
# movies.sort()
# #print(movies)
# print(movies[n-1])


'''
666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 7666, 8666, 9666, 10666, 11666, ...

입력 예시
2

7

9

17

출력 예시
1666

6660

6662

7666
'''