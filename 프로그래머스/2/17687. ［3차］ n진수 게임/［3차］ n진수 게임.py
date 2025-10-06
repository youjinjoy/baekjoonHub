def solution(n, t, m, p):

    # 변환
    result = ''
    i = 0
    while len(result) < m * t:
        result += convert_base(i, n)
        i += 1
    print('result',result)
    # 순회
    answer = ''
    j = 0
    while j < t:
        answer += result[m * j + p - 1]
        j += 1
    
    return answer

base_map = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(number, base):

    
    converted = []
    
    while number // base != 0:
        if number % base >= 10:
            converted.append(base_map[number % base])
        else:
            converted.append(str(number % base))

        number = number // base
    
    if number >= 10:
        converted.append(base_map[number])
    else:
        converted.append(str(number))
    
    converted.reverse()
    
    return ''.join(converted)
