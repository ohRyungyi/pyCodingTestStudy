import sys

N = 9

heights = [int(sys.stdin.readline()) for _ in range(N)]

# print(heights)

tot = sum(heights)

isEnd = False

for i in range(N-1):
    for j in range(i+1, N):
        # print(i, j)
        data = tot - heights[i]-heights[j]

        if data == 100:
            h1 = heights[i]
            h2 = heights[j]
            # print(i, j, heights[i], heights[j])
            heights.remove(h1)
            heights.remove(h2)
            
            heights.sort()

            for height in heights:
                print(height)
            
            isEnd = True
            break
    if isEnd:
        break

    

'''
입력
20
7
23
19
10
15
25
8
13

출력
7
8
10
13
19
20
23
'''