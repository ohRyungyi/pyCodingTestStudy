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

<br>

### 백준 단계별

<br>

### 백준 개별문제
