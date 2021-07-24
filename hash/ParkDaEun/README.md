## 3주차 - Hash

### 프로그래머스
<details>
<summary>완주하지 못한 선수</summary>
<div markdown="1">

</div>
</details>

<details>
<summary>전화번호 목록</summary>
<div markdown="1">
<br>

``` python
def solution(phone_book):
    phone_book.sort() # 문자 정렬은 ["119", "1195524421", "97674223"]와 같이 숫자 크기대로 되는 것이 아님.

    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break

        # 정렬을 했기 때문에 두 글자만 비교함
        prefix = phone_book[i]
        other_num = phone_book[i+1]

        # 접두어가 비교하는 전화번호 맨 앞에 존재할 때
        if prefix in other_num and other_num.index(prefix) == 0:
            return False

    return True

```

- 💡 아이디어
<br>먼저 파이썬 내장 라이브러리를 이용하여 전화번호부를 정렬해준다. 
<br>숫자를 정렬하면 숫자의 크기순대로 정렬되지만, 문자로 정렬하면 ["119", "1195524421", "97674223"]와같이 정렬된다.
<br>따라서 연속되는 두 글자만 비교하면된다. 이는 for문을 사용해서 비교해주었다. <br>각각 변수명은 prefix와 other_num이라 설정해주었다. prefix가 other_num에 존재하고, prefix가 접두어가 맞다면(index(prefix) == 0)이라면 False를 출력하도록 했다.  
<br>

- 📚 후기
<br> 처음엔 이중 for문을 쓰도록 했다. for문 하나는 prefix를 설정해주는 데 사용하였고, 다른 for문을 통해 prefix와 나머지 리스트 내의 모든 전화번호와 비교하였다.<br>이렇게 하니 정확성 테스트는 모두 통과하였지만, 효율성테스트에 3,4번 문제에서 계속 시관초과가 떴다. <br>문자를 정렬하면 저런식으로 정렬이 되는지 몰랐다. 정렬을 사용한 후 앞 뒤 두 글자만 비교하도록 설정했더니 효율성문제가 해결되었다.
<br>

- ✏️ 배운점
  1. 문자열을 정렬하면 숫자 순서대로 정렬되는 게 아니라는 것.
  2. startswith 함수 : 원본 문자열이 매개변수로 입력한 문자로 시작되는지 판단하는 함수(대소문자 구분함) (endswith함수도 있음)
  3. hash를 이용한 다른 사람들 코드
``` python
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```  

</div>
</details>

<details>
<summary>위장</summary>
<div markdown="1">

</div>
</details>

<details>
<summary>베스트앨범</summary>
<div markdown="1">
<br>
    
``` python
def solution(genres, plays):
    songs = {}  # key: 장르  value: [(고유번호, 재생횟수)]
    genres_time = {}  # key: 장르 value: 장르 별 총 재생횟수

    for i in range(len(genres)):
        # songs 내에 장르가 있다면
        if genres[i] in songs:
            # songs 내 장르에 노래 추가
            songs[genres[i]].append([i, plays[i]])

            # 장르 횟수 수가
            genres_time[genres[i]] += plays[i]

        # songs 내에 장르가 없다면
        else:
            # songs에 장르 등록하기
            songs[genres[i]] = [[i, plays[i]]]

            # 장르 횟수 재기 시작
            genres_time[genres[i]] = plays[i]

    # print("SONGS: ", songs)         >> {'classic': {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}
    #print("TIMES: ", genres_time)   >> {'classic': 1450, 'pop': 3100}

    # genres_time을 이용하여 속한 노래가 많이 재생된 장르 순으로 정렬
    genres_order = sorted(list(genres_time.items()), key=lambda x: x[1])
    # 가장 적은 숫자부터 정렬되므로 많이 재생된 장르 순으로 정렬되도록 reverse
    genres_order.reverse()
    #print("ORDER_TIMES: ", genres_order)     >> [('pop', 3100), ('classic', 1450)]

    answer = []
    # 장르 별로 for문
    for g in genres_order:
        # 장르 내에서 많이 재생된 노래 정렬 : x[1] = 재생횟수, x[0] = 고유번호. (재생횟수 순대로 정렬 후, 고유번호 순대로 역순 정렬(reverse할 것이므로))
        plays_order = sorted(songs.get(g[0]), key=lambda x: (x[1], -x[0]))
        # 가장 적은 숫자부터 정렬되므로 많이 재생된 노래 순으로 정렬되도록 reverse
        plays_order.reverse()

        # answer에 장르별 가장 많이 재생된 노래 두개 출력
        answer.append(plays_order[0][0])
        # 장르에 속한 곡이 하나라면 하나만 출력
        if len(plays_order) > 1:
            answer.append(plays_order[1][0])
    return answer
    
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
```    

- 💡 아이디어
    <br> 
<br>
    
- 📚 후기
    <br> 
<br>
    
- ✏️ 배운점
    - sorted_list = sorted(list, key = lambda x: x[1])
<br>
</div>
</details>

<br>

### 백준 단계별
<details>
<summary>1920(수 찾기)</summary>
<div markdown="1">

</div>
</details>

<br>

### 백준 개별문제
<details>
<summary>1620(나는야 포켓몬 마스터 이다솜)</summary>
<div markdown="1">
<br>
    
``` python
import sys

# n: 도감에 등록된 포켓몬 개수
# m: 맞춰야 하는 문제 개수
n, m = map(int, sys.stdin.readline().split())

pocketmons_keyname = {}
pocketmons_keynum = {}

# 도감에 포켓몬 등록하기
for i in range(n):
    pocketmon = sys.stdin.readline().rstrip()  # 입력된 포켓몬
    pocketmons_keyname[pocketmon] = i+1
    pocketmons_keynum[i+1] = pocketmon

# 문제 맞추기
for j in range(m):
    question = sys.stdin.readline().rstrip()  # 포켓몬 맞추는 문제

    # 도감에서 포켓몬 불러오기
    if question.isnumeric() == True:
        print(pocketmons_keynum.get(int(question)))
    else:
        print(pocketmons_keyname.get(question))    
```    

- 💡 아이디어
    <br> 포켓몬 이름을 이용하여 몇 번째 포켓몬인지 검색할 수도 있어야하고, 등록된 순서를 이용하여 무슨 포켓몬인지 검색할 수도 있어야한다. 따라서 딕셔너리를 총 두개 만들었다. 
    <br>(1: poketmons_keyname) key:포켓몬 이름, value:등록 순서 (2: pocketmons_keynum) key:등록 순서, value: 포켓몬 이름
    <br> isnumeric() 함수를 사용해서 문제가 숫자라면 pocketmons_keynum 딕셔너리를 이용하여 검색하였고, 숫자가 아니라면 pocketmons_keyname을 사용해 검색하도록 하였다.
<br>
    
- 📚 후기
    <br> 해시를 알면 굉장히 쉬운 문제지만, 해시를 몰랐다면 리스트를 이용하여 풀려고 시도했을 것 같다. 
    <br>시간제한이 없다면 리스트를 이용해도 문제가 풀릴 것 같다. 하지만 해시가 훨씬 빠르므로 해시를 이용하도록 하자.
<br>
    
- ✏️ 배운점
    - S.isnumeric() : S(문자열)가 숫자로 구성되어있는지 확인하는 함수 (cf: isalpha(), isalnum())
<br>
    
</div>
</details>

<details>
<summary>17264(I AM IRONMAN)</summary>
<div markdown="1">
<br>
    
``` python
import sys

# n: 총 게임 횟수
# p: 해킹을 통해 얻은 플레이어 정보의 수
n, p = map(int, sys.stdin.readline().split())

# w: 이긴 경우 획득 점수
# l: 졌을 때 떨어지는 점수
# g: IRON 티어 벗어나기 위한 점수
w, l, g = map(int, sys.stdin.readline().split())

# 해킹한 선수, 이기는지(W) or 지는지(L) 딕셔너리에 받기
hacked_player = {}
for i in range(p):
    name, t = sys.stdin.readline().split()
    hacked_player[name] = t

# 같이 게임하는 플레이어 이름 받아서 점수 계산하기
point = 0
for j in range(n):
    name = sys.stdin.readline().rstrip()

    if hacked_player.get(name) == 'W':  # 해킹을 해서 무조건 이길 수 있는 확률
        point += w
    else:  # 해킹을 했는데 지는 선수이거나, 해킹 정보가 없는 선수
        point -= l
        if point < 0:  # 점수는 절대 0점 밑으로 떨어지지 않음
            point = 0

    if point >= g:  # 점수가 IRON 티어 벗어나기 위한 점수를 넘겼을 때
        print("I AM NOT IRONMAN!!")
        quit()  # 프로그램 종료

print("I AM IRONMAN!!")
```
    

- 💡 아이디어
    <br> 해킹한 플레이어를 딕셔너리에 받아 이름을 key로 저장하고, 졌는지('L') 이겼는지('W')를 value로 저장하였다.
    <br> n번의 게임횟수 동안 플레이어의 이름이 딕셔너리에 있는지 검사하면서 이겼다면 포인트를 얻고, 지거나 딕셔너리에 없다면 포인트를 잃도록 설정하였다.
<br>
    
- 📚 후기
    <br> w, l로 획득 점수와 잃는 점수 변수를 설정해놓고 예제의 점수로 획득하고 잃도록 계속 코드를 짰다.
    <br> 따라서 예제로는 정답인데 백준에서는 틀렸다고 뜨는 어이없는 실수를 했다.
<br>
    
- ✏️ 배운점
    - quit(): 파이썬 프로그램 종료. (c언어에서 return 0과 비슷)
<br>
    
</div>
</details>

<details>
<summary>3077(임진왜란)</summary>
<div markdown="1">
<br>
    
``` python
import sys
import itertools  # 조합

# n: 해전의 개수
n = int(sys.stdin.readline())

# 해전 순서의 정답
wars_correct = dict(zip(sys.stdin.readline().split(), [i for i in range(n)]))

# 학생의 답안
wars_answer = sys.stdin.readline().split()

# 학생의 답안 중 N(N-1)/2개의 쌍 고름
pick = list(itertools.combinations(wars_answer, 2))
''' >>> 출력: [('sacheon', 'hansan'), ('sacheon', 'myeongnyang'), ('sacheon', 'noryang'), ('sacheon', 'okpo'), ('hansan', 'myeongnyang'),
 ('hansan', 'noryang'), ('hansan', 'okpo'), ('myeongnyang', 'noryang'), ('myeongnyang', 'okpo'), ('noryang', 'okpo')]
'''
point = 0  # 학생의 점수
# N(N-1)/2개의 쌍 중에서 해전이 일어난 연도의 순서를 맞게 적었다면 +1점
for p in pick:
    if wars_correct.get(p[0]) < wars_correct.get(p[1]):
        point += 1

# 학생 점수/총 점수
print("%d/%d" % (point, n*(n-1)/2)) 
```                                                    

- 💡 아이디어
    <br> 해전이 일어난 순서대로 정답이 받아지므로, 해전 이름을 key, 순서를 value로 하여 딕셔너리로 받았다.
    <br> 학생의 답안 중 N(N-1)/2개의 쌍을 전부 검사하여 순서가 맞았는지 틀렸는지 검사하므로 이를 itertools.combination을 이용하여 조합을 만들었다.
    <br> 만든 조합을 for문을 사용하여 검사하며, 맞았을 시 point를 +1하였다.
<br>
    
- 📚 후기
    <br> 시간제한이 1초길래 정말 모든 경우의 수를 찾는 게 맞나? 라는 생각을 했는데 그게 맞았다.
    <br> 해시를 이용해 최대한 시간을 줄이는 것이 관건이었던 것 같다.
<br>
    
- ✏️ 배운점
    - dict(zip(list1, list2)): list 두 개를 이용하여 딕셔너리로 만듦. list1은 key, list2는 value가 됨.
    - itertools: 경우의 수를 찾을 때 사용되는 라이브러리 (import itertools)
        - itertools.permutations: 순서는 중요하고 중복은 허용되지 않음. 
          <br>ex) itertools.permutations([1, 2, 3], 2) => [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
        - itertools.product: 순서는 중요하고 중복은 허용됨.
          <br>ex) itertools.product([1, 2, 3], 2) => [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
        - itertools.combinations: 순서는 중요하지 않고 중복은 허용되지 않음.
          <br>ex) itertools.combinations([1, 2, 3], 2) => [(1,2), (1,3), (2,3)]
        - itertools.combinations_with_replacement: 순서는 중요하지 않고 중복은 허용됨.
          <br>ex) itertools.combinations_with_replacement([1, 2, 3], 2) => [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]
<br>

</div>
</details>
