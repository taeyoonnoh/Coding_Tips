def solution(sizes):
    max_w,max_h = 0,0
    for size in sizes : 
        size.sort()
        check_w,check_h = size
        max_w = max(check_w,max_w)
        max_h = max(check_h,max_h)
    return max_w * max_h
