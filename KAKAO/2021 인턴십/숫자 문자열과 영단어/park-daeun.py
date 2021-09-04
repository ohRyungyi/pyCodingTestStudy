def solution(s):
    if "zero" in s:
        s = s.replace("zero", "0")
    if "one" in s:
        s = s.replace("one", "1")
    if "two" in s:
        s = s.replace("two", "2")
    if "three" in s:
        s = s.replace("three", "3")
    if "four" in s:
        s = s.replace("four", "4")
    if "five" in s:
        s = s.replace("five", "5")
    if "six" in s:
        s = s.replace("six", "6")
    if "seven" in s:
        s = s.replace("seven", "7")
    if "eight" in s:
        s = s.replace("eight", "8")
    if "nine" in s:
        s = s.replace("nine", "9")

    return int(s)

s = "one4seveneight"
print(solution(s))

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