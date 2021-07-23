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

'''
입력 예시
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

출력 예시
[4, 1, 3, 0]
'''
