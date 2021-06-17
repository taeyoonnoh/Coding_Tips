def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) : 
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] : 
            return False
    return True

# 접두사란 무조건 앞에 해당 단어를 포함하느냐를 보는 것
# 처음에 sorting을 시켜주면 i 번째와 i+1 번째끼리만 비교하면 빨리 찾을 수 있음!
