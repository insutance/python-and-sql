"""
처음 작성한 코드
"""
def solution(genres, plays):
    totalPlays = {}     # 각 장르별 총 play 횟수
    eachPlays = {}      # 장르별 각각의 play 횟수

    i = 0
    for genre, play in zip(genres, plays):      
        if genre in totalPlays.keys():          # genre가 이미 totalPlays 안에 있다면
            totalPlays[genre] += play           # play 횟수를 더해줌 (총 play 횟수 구하기 위해)
            eachPlays[genre].append([i, play])  # [i(고유번호), play]
        else:
            totalPlays[genre] = play            # genre가 totalPlays에 없다면 생성
            eachPlays[genre] = [[i, play]]
        i += 1  

    # totalPlays Dictionary에서 play가 많이 된 순서대로 정렬
    totalPlays = sorted(totalPlays.items(), key = lambda item: item[1], reverse=True)
    answer = []
    for key in totalPlays:      # 정렬된 totalPlays로 for문 시작
        # key[0] = genre // eachPlays Diationary에서 play가 많이 된 순서대로 정렬, 이때 값이 같다면 자동으로 고유번호 먼저인 것이 앞으로 정렬됨.
        eachPlays[key[0]] = sorted(eachPlays[key[0]], key=lambda item: item[1], reverse=True)
        
        if len(eachPlays[key[0]]) == 1 :                
            answer.append(eachPlays[key[0]][0][0])      # 길이가 1이면 첫번째 고유번호를 저장
        else:                                           
            for i in range(2):                          
                answer.append(eachPlays[key[0]][i][0])  # 길이가 1보다 크면 for문을 돌면서 고유번호 저장
    
    return answer

"""
수정한 코드
"""
def solution3(genres, plays):
    totalPlays = {}     # 각 장르별 총 play 횟수
    eachPlays = {}      # 장르별 각각의 play 횟수

    for i in range(len(genres)):
        if genres[i] not in totalPlays:             # genre가 totalPlays에 없다면
            totalPlays[genres[i]] = 0               # key값을 만들어 주고 0으로 초기화
            eachPlays[genres[i]] = []               # key값을 만들어 주고 [] 빈배열 생성

        totalPlays[genres[i]] += plays[i]           # 해당 genre(key값)에 play를 더해줌.
        eachPlays[genres[i]].append([i, plays[i]])  # 해당 genre(key값)에 [i(고유번호), play] 를 추가
    
    # totalPlays Dictionary에서 play가 많이 된 순서대로 정렬
    totalPlays = sorted(totalPlays.items(), key=lambda tuple: tuple[1], reverse=True)

    answer = []
    # 정렬된 totalPlays로 for문을 돌려준다.
    for genre, play in totalPlays:
        # eachPlays Diationary에서 play가 많이 된 순서대로 정렬
        # 이때 값이 같다면 자동으로 고유번호 먼저인 것이 앞으로 정렬됨.
        eachPlays[genre] = sorted(eachPlays[genre], key=lambda list: list[1], reverse=True)

        # 각 eachPlays[genre]에서 2번째까지만 가지고와 해당 고유번호를 extend해준다.
        # 1개만 있는 장르는 1개만 가져오게 된다.
        answer.extend([index for index, play in eachPlays[genre][:2]])  
    
    return answer

"""
도움이 된 코드
"""
def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer

print(solution3(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))