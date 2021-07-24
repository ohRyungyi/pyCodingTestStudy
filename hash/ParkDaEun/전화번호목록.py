def solution(phone_book):
    # 문자 정렬은 ["119", "1195524421", "97674223"]와 같이 숫자 크기대로 되는 것이 아님.
    phone_book.sort()

    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break

        # 정렬을 했기 때문에 두 글자만 비교함
        prefix = phone_book[i]
        other_num = phone_book[i+1]

        # 접두어가 비교하는 전화번호 맨 앞에 존재할 때
        if prefix in other_num and other_num.index(prefix) == 0:
            return False

    '''for i in range(len(phone_book)):
        prefix = phone_book[0]
        phone_book.remove(prefix)

        if len(phone_book) == 0:
            break

        if prefix in phone_book[0] and phone_book[0].index(prefix) == 0:
            return False'''

    return True


phone_book = ["123", "456", "789"]
print(solution(phone_book))

'''
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        prefix = phone_book[0]
        phone_book.remove(prefix)

        for phone_num in phone_book:
            if phone_num[0] != prefix[0]:
                break

            if prefix in phone_num and phone_num.index(prefix) == 0:
                return False

    return True
'''

'''
입력 예시
phone_book = ["119", "97674223", "1195524421"]

phone_book = ["123","456","789"]

phone_book = ["12","123","1235","567","88"]

출력 예시
false

true

false
'''
