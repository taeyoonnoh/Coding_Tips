import heapq

def solution(m, musicinfos):
    answer = []
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

    for info in musicinfos : 
        start,end,title,melody = info.split(',')
        start_hour,start_minute = map(int,start.split(':'))
        end_hour,end_minute = map(int,end.split(":"))
        melody = melody.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        time = 60 * (end_hour-start_hour) + (end_minute-start_minute)
        melody = (melody * time)[:time]
        if m in melody : 
            heapq.heappush(answer,(-time,title))
    if answer : 
        return heapq.heappop(answer)[1]
    else :
        return "(None)"
  
  # ===================================================================================================================
  # #이 포함되어 있으면 처리하기가 어려울 수 있으므로 소문자로 대체
  # 멜로디가 반복되기 때문에 time 변수 생성해서 길이 늘려주기
  # heapq 활용해서 해당하는 곡들 담기
  # 재생된 시간 가장 긴 음악제목 반환!
