def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        phone = phone_book[i]
        next_phone = phone_book[i+1]
        if len(phone) <= len(next_phone):
            if phone == next_phone[:len(phone)]:
                return False
    return answer