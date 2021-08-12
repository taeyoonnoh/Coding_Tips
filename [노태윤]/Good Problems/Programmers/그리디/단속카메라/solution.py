def solution(routes):
    routes = sorted(routes,key=lambda x : x[1])
    camera = -30000
    answer = 0
    for route in routes :
        if camera < route[0] : # 카메라 위치가 다음 route 의 최소값보다 낮다면 카메라 위치 추가가능하다는 뜻!
            camera = route[1] # 카메라 위치 업데이트
            answer+=1
    return answer
