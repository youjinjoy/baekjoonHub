def solution(s):
    test1 = s.split('{{')[1].split('}}')[0].split('},{')
    test2 = [i.split(',') for i in test1]
    test3 = sorted(test2, key = len)
    
    result = []
    for tuples in test3:
        for value in tuples:
            if not value in result:
                result.append(value)
            
    return list(map(int, result))