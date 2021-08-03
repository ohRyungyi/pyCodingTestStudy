import sys

N = int(sys.stdin.readline())

data='666'

# for i in range(N):
#     if i ==0 :
#         # print(data)
#         pass
#     else:
#         data = data.split('666')

#         if data[1] == '' and data[0] == '':
#             data = '1666'

#         elif data[1] == '':
#             # ~666
#             temp = str(int(data[0])+1)
#             data = ''.join([temp, '666', data[1]])

#             if temp[-1]== '6':
#                 # ~6666
#                 data = data.split('666')
#                 temp = data[1].replace('6', '0')

#                 data= ''.join([data[0], '666', temp])

#                 # print('1',data)

#         else:

#             if len(str(int(data[1]))) < len(str(int(data[1])+1)):
#                 top = data[0]+'7'
#                 data = ''.join([top, '666', ''])
#             else:
#                 data = ''.join([data[0], '666', str(int(data[1])+1)])

data = 666

while True:
    if str(data).find('666') != -1:
        if N == 1:
            print(data)
            break
        else:
            N-=1
    
    data+=1





# print(data)


'''
입력
2

출력
1666
'''