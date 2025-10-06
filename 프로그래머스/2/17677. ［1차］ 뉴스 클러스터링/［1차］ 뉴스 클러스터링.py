def solution(str1, str2):
    answer = 0

    dict1 = make_dict(str1)
    dict2 = make_dict(str2)
    
    union = 0
    intersection = 0
    
    for key in dict1.keys():
        if dict2.get(key):
            intersection += min(dict1[key], dict2[key])
            union += max(dict1[key], dict2[key])
    
    for key in dict1.keys():
        if not dict2.get(key):
            union += dict1[key]

    for key in dict2.keys():
        if not dict1.get(key):    
            union += dict2[key]

    if union == 0:
        return 65536
    
    return int((intersection * 65536) / union)

def make_dict(S):
    dict = {}
    p1, p2 = 0, 1

    while p2 < len(S):
        ch1, ch2 = S[p1], S[p2]

        if not ch2.isalpha():
            p1 += 2
            p2 += 2
            continue

        if not ch1.isalpha():
            p1 += 1
            p2 += 1
            continue

        word = S[p1:p2+1].lower()
        print("W",word)

        if dict.get(word):
            dict[word] += 1
        else:
            dict[word] = 1

        p1 += 1
        p2 += 1

    return dict