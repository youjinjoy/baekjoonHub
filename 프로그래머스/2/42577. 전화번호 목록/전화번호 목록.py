def solution(phone_book):
    answer = True
    
    prefix = {n: True for n in phone_book}
    
    for number in phone_book:
        p = ''
        for i in range(len(number)):
            p += number[i]
            if prefix.get(p) and p != number:
                return False
    
    return answer