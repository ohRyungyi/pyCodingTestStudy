def solution(s):
    print(s.count("one"))
    if s.count("zero") > 0:
        s.replace("zero", "0")
    if "one" in s:
        s.replace("one", "1")
    if s.count("two") > 0:
        s.replace("two", "2")
    if s.count("three") > 0:
        s.replace("three", "3")
    if s.count("four") > 0:
        s.replace("four", "4")
    if s.count("five") > 0:
        s.replace("five", "5")
    if s.count("six") > 0:
        s.replace("six", "6")
    if s.count("seven") > 0:
        s.replace("seven", "7")
    if s.count("eight") > 0:
        s.replace("eight", "8")
    if s.count("nine") > 0:
        s.replace("nine", "9")

    return int(s)

s = "one4seveneight"
solution(s)

'''
입력 예시
"one4seveneight"

"23four5six7"

"2three45sixseven"

"123"

출력 예시
1478

234567

234567

123
'''