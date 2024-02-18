from collections import Counter

def solution(participant, completion):
    # Counter를 이용하여 각 선수의 참여자 수를 계산
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    # 참여자 명단과 완주자 명단의 Counter를 빼서 남은 참여자를 찾음
    answer_counter = participant_counter - completion_counter

    # Counter의 elements 메서드를 사용하여 남은 참여자 중 첫 번째 이름을 반환
    answer = list(answer_counter.elements())[0]

    return answer